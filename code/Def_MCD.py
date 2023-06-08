def mcd(resultadoN, resultadoD):
    global resultadoN
    global resultadoD
    c = 1
    if resultadoN > resultadoD:
        f = resultadoN
    else:
        f = resultadoD
    while c != 0:
        f = f - 1
        d = resultadoN % f
        e = resultadoD % f
        if d == 0 and e == 0:
            c = 0

    resultadoD = resultadoD / f
    resultadoN = resultadoN / f
    print(f"{resultadoN} / {resultadoD}")
