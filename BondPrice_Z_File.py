

def getBondPrice_Z(face, couponRate, times, yc):
    
    bondPrice = 0
    c = face * couponRate

    for t, rate in zip(times, yc):

        cf = c
        if t == times[-1]:
            cf = cf + face

        pv = cf / ((1 + rate) ** t)
        bondPrice = bondPrice + pv

    return(bondPrice)