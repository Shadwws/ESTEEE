a = 0
b = 2
sumaN = 0
sumaD = 1
restaN = 0
restaD = 1
multiN = 1
multiD = 1
x = 0
i = 0
op = ""

while op != "=":

    if a == 0:
        num = int(input("numerador"))
        den = int(input("denominador"))
        if num < 0:
            op = "-"
        else:
            op = "+"
        a = 1
    else:
        print("elija el operador a usar")
        print("ingrese + para sumar")
        print("ingrese - para restar")
        print("ingrese x para multiplicar")
        print("ingrese / para dividir")
        op = str(input(""))

        if op != "=":
            num = int(input("numerador "))
            den = int(input("denominador "))

    if op == "+":
        if x == 1:
            multiN = multiN * num
            multiD = multiD * den
            sumaN = (sumaN * multiD) + (multiN * sumaD)
            sumaD = sumaD * multiD
            x = 1
            multiN = 1
            multiD = 1
        else:
            sumaN = sumaN * den + num * sumaD
            sumaD = sumaD * den
            an = num
            ad = den
            i = 1
        add = sumaD

    elif op == "-":
        print("no disponible, lo siento")

    elif op == "x":
        if i == 1:
            sumaN = sumaN * ad - sumaN * add
            sumaD = sumaD / add
            multiN = multiN * an
            multiD = multiD * ad
            i = 0
        else:
            multiN = multiN * num
            multiD = multiD * den
            x = 1

    elif op == "/":
        print("no disponible, lo siento")

    elif op != "=":
        print("valor erroneo, intentar de nuevo")

m1 = multiN * num
m2 = multiD * den
t = m1 * sumaD
resultadoN = sumaN * m2 + t
resultadoD = sumaD * m2
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

print("gracias por usar el programa!!")
resultadoD = resultadoD / f
resultadoN = resultadoN / f
print(f"{resultadoN} / {resultadoD}")