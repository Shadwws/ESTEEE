def dym(num, den):
    den = 0
    global multiD
    global multiN
    while den == 0:
        num = int(input("ingrese numerador"))
        den = int(input("ingrese denominador"))
    multiN = multiN * num
    multiD = multiD * den

    op = str(input("desea salir Y/N"))
    if op.lower() == "y":
        op = "="
