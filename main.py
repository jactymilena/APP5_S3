from rsa import *
from dh import *
from flux import *

# Decryption des facteurs q p et g avec RSA
q, p, g = decrypter_qpg()
# Puissances g^x
power = puissances(p, g)

print(power)

# Cle symetrique (DH) est la premiere du tableau car l'autre c'est 1 donc 1 * g^x = g^x
cle = power[0]
# Decryption par flux
chiffre_flux(cle, "salaires.mm", "sortie.txt")
# Decryption des salaires avec RSA
decrypter_salaires()
