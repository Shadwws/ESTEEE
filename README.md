operacion = ""
cuenta_total = ""
print ("Usted a seleccionado la calculadora clásica.")
resultado = float(input("Ingrese valor inicial: "))
cuenta_total = (f"{resultado}")
while operacion != "=":
    operacion = input(f"Tiene el número {resultado}, qué operación desea hacer?\n\nIngrese '+' para sumar,\nIngrese '-' para restar,\nIngrese '/' para dividir,\nIngrese '*' para multiplicar, \nIngrese '=' para obtener el resultado final:\n")
    if operacion == "+":
        num = float(input("Ingrese número a sumar:  "))
        resultado += num
        cuenta_total += (f" + {num}")
    if operacion == "-":
        num = float(input("Ingrese número a restar:  "))
        resultado -= num
        cuenta_total += (f" - {num}")
    if operacion == "/":
        num = float(input("Ingrese número a dividir:  "))
        resultado /= num
        cuenta_total += (f" / {num}")
    if operacion == "*":
        num = float(input("Ingrese número a multiplicar:  "))
        resultado *= num
        cuenta_total += (f" * {num}")
cuenta_total += (f" = {resultado}")
print (f"Usted a realizado la siguiente cuenta: \n{cuenta_total}\nEl resultado final es: {resultado}")
