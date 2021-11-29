
def puissances(p, g):
    print('Trouver les puissances')
    power = []
    for i in range(1, p):
        calcul = pow(g, i, p)

        if calcul != 0:
            power.append(calcul)

        if calcul == 1:
            return power

    return power
