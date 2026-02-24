def getBondDuration(y, face, couponRate, m, ppy = 1):

    n = int(m * ppy)
    r = y / ppy
    c = face * couponRate / ppy

    pv_sum = 0
    tpv_sum = 0

    t = 1
    while t <= n:

        cf = c
        if t == n:
            cf = cf + face

        pv = cf / ((1 + r) ** t)

        pv_sum = pv_sum + pv
        tpv_sum = tpv_sum + (t / ppy) * pv

        t = t + 1

    bondDuration = tpv_sum / pv_sum
    return(bondDuration)