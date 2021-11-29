'''
Created on 2009-07-14

@author: Administrateur
'''

import os.path
import array

# Extraire un masque de 8 bits de la cle
def get_masque_8bits(cle):
    return cle & 0b11111111


# Preparer la cle pour la prochaine iteration
def get_cle_modifiee(cle):
    return cle >> 8


# Chiffrer le caractere
def chiffre_caractere(caractere,masque):
    return caractere ^ masque


# Mettre a jour la cle au besoin
def mise_a_jour_cle(tmpcle,cle):
    return cle if tmpcle == 0 else tmpcle


# Methode de chiffrement / dechiffrement par flux
# La cle est utilisee pour chiffrer le fichier d'entree (fichierin) et produire le fichier de sortie (fichierout)
# Si la cle est plus petite que la taille du fichier, elle doit etre repetee (est-ce une bonne idee?)
def chiffre_flux(cle,fichierin,fichierout):
    tmpcle = cle
    
    # Initialisation des fichiers en lecture et ecriture
    infileobj = open(fichierin,'rb')     # Lecture binaire du fichier
    outfileobj = open(fichierout,'wb')   # Ecriture binaire du fichier
    filesize = os.path.getsize(fichierin)
    
    # Initialisation des tableaux binaires, lecture du fichier d'entree (binaire)
    inbinvalues = array.array('B')
    inbinvalues.fromfile(infileobj, filesize)
    outbinvalues = array.array('B')
    
    # Traitement de tous les caracteres du fichier d'entree, un a la fois
    i = 0
    while (i < filesize):
        # Obtention du masque pour le prochain caractere, chiffrement de ce caractere
        mask = get_masque_8bits(tmpcle)
        tmpcle = get_cle_modifiee(tmpcle)
        newchar = chiffre_caractere(inbinvalues[i], mask)
        # Ecriture du cactere chiffre dans le tampon de sortie
        outbinvalues.append(newchar)
        
        i += 1
        tmpcle = mise_a_jour_cle(tmpcle,cle)

    # Ecriture dans le fichier de sortie, fermeture des fichiers
    infileobj.close()
    outbinvalues.tofile(outfileobj)
    outfileobj.close()
