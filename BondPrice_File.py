

def getBondPrice(y, face, couponRate, m, ppy = 1):

    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy

    bondPrice = 0

    t = 1
    while t <= n:
        cf = c
        if t == n:
            cf = cf + face

        pv = cf / ((1 + r) ** t)
        bondPrice = bondPrice + pv

        t = t + 1

    return(bondPrice)