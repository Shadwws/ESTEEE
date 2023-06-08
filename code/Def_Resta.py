def restas(num, den):
    global restaD
    global restaN
    global op
    while op != "=":
        den = 0
        while den == 0:
            num = int(input("ingrese numerador"))
            den = int(input("ingrese denominador"))
        restaN = num * restaD - restaN * den
        restaD = restaD * den
        op = str(input("Ingrese = para mostrar el resultado, o apriete cualquier cosa para seguir sumando"))

