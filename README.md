def calculadora_clasica():
    operacion = ""
    cuenta_total = ""
    print ("\nUsted a seleccionado la calculadora clásica.")
    resultado = float(input("Ingrese valor inicial: "))
    cuenta_total = (f"{resultado}")
    while operacion != "=":
        operacion = input(f"\nTiene el número {resultado}, qué operación desea hacer?\n\nIngrese '+' para sumar,\nIngrese '-' para restar,\nIngrese '/' para dividir,\nIngrese '*' para multiplicar, \nIngrese '=' para obtener el resultado final:\n")
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
    print (f"\nUsted a realizado la siguiente cuenta: \n{cuenta_total}\nEl resultado final es: {resultado}")
    
#def menu_inicial es el menù principal del programa
def menu_inicial():
    iniciar = ""
    cual = 0
    while iniciar != "on":
        iniciar  = input("Ingrese 'On' para iniciar calculadora: \n")
        iniciar = iniciar.lower()
    print ("\nSe ha iniciado la calculadora.")
    while cual != 4:
        cual = int(input("\nMenù de la calculadora:\nIngrese 1 si desea utilizar la calculadora clàsica.\nIngrese 2 si desea utilizar la calculadora de fracciones.\nIngrese 3 si desea utilizar la calculadora de conversiones.\nIngrese 4 si desea apagar la calculadora.\nElija su opciòn: "))
        if cual == 1:
            calculadora_clasica()
        elif cual == 2:
            menu_de_fracciones()
        elif cual == 3:
            menu_de_conversion()
    print ("\n\nA seleccionado apagar la calculadora. \nMuchas gracias.")
    
menu_inicial()
