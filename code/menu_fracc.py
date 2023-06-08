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

        else:
            dym(0, 0)


    elif op != "=":
        print("valor erroneo, intentar de nuevo")

mcd(0, 0)