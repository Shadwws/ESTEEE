a = 0
b = 0
op = ""
l = 0
resultadoD = 0
resultadoN = 1
num = 1
den = 0


def sumas(num, den):
    global op
    global resultadoD
    global resultadoN

    while op != "=":
        den = 0
        while den == 0:
            num = int(input("ingrese numerador  \n"))
            den = int(input("ingrese denominador  \n"))
        resultadoN = num * resultadoD + resultadoN * den
        resultadoD = resultadoD * den
        op = str(input("Ingrese = para mostrar el resultado, o apriete cualquier cosa para seguir sumando"))
        mcd(resultadoN, resultadoD)


def restas(num, den):
    global resultadoD
    global resultadoN
    global op
    while op != "=":
        den = 0
        while den == 0:
            num = int(input("ingrese numerador \n"))
            den = int(input("ingrese denominador \n"))
        resultadoN = num * resultadoD - resultadoN * den
        resultadoD = resultadoD * den
        op = str(input("Ingrese = para mostrar el resultado, o apriete cualquier cosa para seguir sumando"))
        mcd(resultadoN, resultadoD)


def dym(num, den):
    den = 0
    global op
    global resultadoD
    global resultadoN


    while den == 0:
        num = int(input("ingrese numerador  \n"))
        den = int(input("ingrese denominador  \n"))
    if l == 1:
        a = num
        b = den
        num = b
        den = a
        resultadoN = resultadoN * num
        resultadoD = resultadoD * den
    else:
        resultadoN = resultadoN * num
        resultadoD = resultadoD * den

    op = str(input("desea salir Y/N"))
    if op.lower() == "y":
        op = "="
    else:
        op="*"
    mcd(resultadoN, resultadoD)


def mcd(resultadoN, resultadoD):
    c = 1
    if resultadoN > resultadoD:
        f = resultadoN + 1
    else:
        f = resultadoD + 1
    while c != 0:
        f = f - 1
        d = resultadoN % f
        e = resultadoD % f
        if d == 0 and e == 0:
            c = 0

    resultadoD = resultadoD // f
    resultadoN = resultadoN // f
    alpha = resultadoN / resultadoD
    print(f"El resultado en fracciones es {resultadoN} / {resultadoD}")
    print(f"El resultado en decimales es {alpha} ")


while op != "=":
    while resultadoD == 0:
        resultadoN = int(input("ingrese numerador  \n"))
        resultadoD = int(input("ingrese denominador  \n"))

    print("ingrese:")
    print("+ para sumar")
    print("- para restar")
    print("/ para dividir")
    print("* para multiplicar")
    op = str(input(""))

    if op == "+":
        sumas(0, 0)


    elif op == "-":
        restas(0, 0)


    elif op == "/":
        op = "*"
        l = 1

    if op == "*":
        while op != "=":
            dym(0, 0)


    elif op != "=":
        print("valor erroneo, intentar de nuevo")

