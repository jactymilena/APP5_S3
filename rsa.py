from itertools import count
from math import gcd
import random
import math


def pgcd(a, n):
    if n < a:
        t = n
        n = a
        a = t
    r = n % a
    while r != 0:
        n = a
        a = r
        r = n % a

    return a


def exposant_modulaire(base, exponent, modulus):
    result = 1

    while exponent > 0:
        if exponent & 1:
            result = (result * base) % modulus

        exponent = exponent >> 1
        base = (base * base) % modulus

    return result


def pollard_rho(n):
    print('pollard')
    m = 2
    for i in range(1, n):
        m = (m ** i) % n
        if pgcd(n, m - 1) != 1:
            p = pgcd(n, m - 1)
            return p


def factoriser(n):
    p = pollard_rho(n)
    q = n // p

    return p, q


def phi_n(p, q):
    return (p-1)*(q-1)


def inverse_multiplicatif(e, n):
    if(e < 0):
        return 'Erreur e plus petit que 0'

    h_g = n
    h_u = 1
    h_v = 0
    b_g = e
    b_u = 0
    b_v = 1

    while b_g != 0:
        t = h_g // b_g

        t_g = b_g
        b_g = h_g - t * b_g
        h_g = t_g

        t_u = b_u
        b_u = h_u - t * b_u
        h_u = t_u

        t_v = b_v
        b_v = h_v - t * b_v
        h_v = t_v

    return h_v


def calcul_d(e_inverse, phi_n):
    return e_inverse % phi_n


def rsa(n, e, c):
    p, q = factoriser(n)
    phi_de_n = phi_n(p, q)
    e_inverse = inverse_multiplicatif(e, phi_de_n)
    d = calcul_d(e_inverse, phi_de_n)

    return exposant_modulaire(c, d, n)

def decrypter_salaires():
    file = open('sortie.txt','rb')     # Lecture binaire du fichier
    print()
    # Paramatres pour dechiffrer les salaires
    n_rsa = 86062381025757488680496918738059554508315544797
    e_rsa = 13
    rsa(n_rsa, e_rsa, file) # file -> contenu du fichier

def decrypter_qpg():
    # Parametres pour dechiffrer (p,q,g)
    n_dh = 71632723108922042565754944705405938190163585182073827738737257362015607916694427702407539315166426071602596601779609881448209515844638662529498857637473895727439924386515509746946997356908229763669590304560652312325131017845440601438692992657035378159812499525148161871071841049058092385268270673367938496513
    e_dh = 1009
    c_q = 70785482415899901219256855373079758876285923471951840038722877622097582944768442919300478197733262514534911901131859013939654902078384994979880540719293485131574905521151256806126737353610928922434810670654618891838295876181905553857594653764136067479449117470741836721372149447795646290103141292761424726007
    c_p = 55044587110698448189468021909149190373421069219506981148292634221985403129928367209713497911359302701069378532959510957622709061077384648566361893749771744973388835727259855002207844685526295296408852878202498675158924213264474587673461598376054133832370354928763624202425050121409987087150490459351809040858
    c_g = 43089172300844684958445369204000423742543038862350925279569289644298734265625491619486408239703259462606739540181409010715678916496299388069246398890469779970287613357772582024703107603034996120914490203805569384580718393586094166173301167583379300330660182750028000520221960355249560831414918130647224546308

    # print(factoriser(n_dh))
    m_q = rsa(n_dh, e_dh, c_q)
    m_p = rsa(n_dh, e_dh, c_p)
    m_g = rsa(n_dh, e_dh, c_g)

    print(f"q : {m_q} \np : {m_p} \ng : {m_g}")

    return m_q, m_p, m_g

