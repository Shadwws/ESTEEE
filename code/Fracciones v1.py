a = 0
b = 0
sumaN = 1
sumaD = 1
restaN = 1
restaD = 1
multiN = 1
multiD = 1
op = ""
l = 0
resultadoD = 0
resultadoN = 0


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


def mcd(resultadoN, resultadoD):
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



while op != "=":
    print("ingrese:")
    print("+ para sumar")
    print("- para restar")
    print("/ para dividir")
    print("* para multiplicar")
    op = str(input(""))

    if op == "+":
        sumas(resultadoN, resultadoD)


    elif op == "-":
        restas(0, 0)
        resultadoN = restaN
        resultadoD = restaD

    elif op == "/":
        op = "x"
        l = 1

    elif op == "*":
        if l == 1:
            a = num
            b = den
            num = b
            den = a
            dym(0, 0)
            resultadoN = multiN
            resultadoD = multiD
        else:
            dym(0, 0)
            resultadoN = multiN
            resultadoD = multiD

    elif op != "=":
        print("valor erroneo, intentar de nuevo")

mcd(0, 0)