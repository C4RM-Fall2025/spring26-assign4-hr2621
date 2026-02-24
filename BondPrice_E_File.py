

def getBondPrice_E(face, couponRate, yc):

    bondPrice = 0
    c = face * couponRate
    
    for t, rate in enumerate(yc, start = 1):

        cf = c
        if t == m:
            cf = cf + face

        pv = cf / ((1 + rate) ** t)
        bondPrice = bondPrice + pv

    return(bondPrice)