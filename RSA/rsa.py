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
    # initialize result
    result = 1

    while (exponent > 0):

        # if y is odd, multiply base with result
        if (exponent & 1):
            result = (result * base) % modulus

        # exponent = exponent/2
        exponent = exponent >> 1

        # base = base * base
        base = (base * base) % modulus

    return result

def PollardRho(n):
    print('pollard')
    if n == 1:
        return n

    if n % 2 == 0:
        return 2

    x = (random.randint(0, 2) % (n - 2))
    y = x
    c = (random.randint(0, 1) % (n - 1))
    d = 1

    while d == 1:
        x = (exposant_modulaire(x, 2, n) + c + n) % n
        y = (exposant_modulaire(y, 2, n) + c + n) % n
        y = (exposant_modulaire(y, 2, n) + c + n) % n

        d = math.gcd(abs(x - y), n)

        if d == n:
            return PollardRho(n)

    return d

def factoriser(n):
    p = PollardRho(n)
    q = n // p

    return p, q

def factoriser_pollard_moins1():
    print('moins1')

def phi_n(p, q):
    print('phi(n)')
    return (p-1)*(q-1)

def inverse_multiplicatif(e, n):
    print('inverse_multiplicatif')
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


# Parametres pour dechiffrer (p,q,g)
n_dh = 71632723108922042565754944705405938190163585182073827738737257362015607916694427702407539315166426071602596601779609881448209515844638662529498857637473895727439924386515509746946997356908229763669590304560652312325131017845440601438692992657035378159812499525148161871071841049058092385268270673367938496513
e_dh = 1009
c_q = 70785482415899901219256855373079758876285923471951840038722877622097582944768442919300478197733262514534911901131859013939654902078384994979880540719293485131574905521151256806126737353610928922434810670654618891838295876181905553857594653764136067479449117470741836721372149447795646290103141292761424726007
c_p = 55044587110698448189468021909149190373421069219506981148292634221985403129928367209713497911359302701069378532959510957622709061077384648566361893749771744973388835727259855002207844685526295296408852878202498675158924213264474587673461598376054133832370354928763624202425050121409987087150490459351809040858
c_g = 43089172300844684958445369204000423742543038862350925279569289644298734265625491619486408239703259462606739540181409010715678916496299388069246398890469779970287613357772582024703107603034996120914490203805569384580718393586094166173301167583379300330660182750028000520221960355249560831414918130647224546308

# Paramatres pour dechiffrer les salaires
n_rsa = 86062381025757488680496918738059554508315544797
e_rsa = 13
c_rsa = 8606238102575748868049691873805954353534535554508315544797 # nombre aléatoire pour tester
print(rsa(n_rsa, e_rsa, c_rsa))

