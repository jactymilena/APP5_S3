from rsa import *

def puissances(p, g):
    print('Trouver les puissances')
    power = []

    for i in range(p):
        power.append(pow(g, i, p))

    print(list(set(power)))


p, q, g = decrypter_qpg()
# p = 17
# g = 86062381025757488680496918738059554508315544797

puissances(p, g)
