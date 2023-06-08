def sumas(num, den):
    global op
    global sumaD
    global sumaN

    while op != "=":
        den = 0
        while den == 0:
            num = int(input("ingrese numerador"))
            den = int(input("ingrese denominador"))
        sumaN = num * sumaD + sumaN * den
        sumaD = sumaD * den
        op = str(input("Ingrese = para mostrar el resultado, o apriete cualquier cosa para seguir sumando"))
        resultadoD = sumaD
        resultadoN = sumaN