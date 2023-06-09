#Trabajo final de IIC: Calculadora


#Variables
a = 0 
b = 0 
op = "" 
l = 0 
resultadoD = 0 
resultadoN = 1 
num = 1 
den = 0


#Convertir Decimales a Binarios

def decimal_a_binario (numero_decimal):
   
    binario = "" 
    
    if numero_decimal != 0:  
        while numero_decimal > 0: 
            residuo = numero_decimal % 2 
            binario = str(residuo) + binario 
            numero_decimal = numero_decimal // 2 
        print(f"\nSu número es igual a:\n{binario}(2)")
    else:
        binario = "0(2)"
        print(f"Su número es igual a {binario}")
    
    
#Convertir Decimales a octales   
    
def decimal_a_octal (numero_decimal):
  
    octal = "" 
  
    if numero_decimal != 0: 
        while numero_decimal > 0: 
            residuo = numero_decimal % 8 
            octal = str(residuo) + octal 
            numero_decimal = numero_decimal // 8 
        print(f"\nSu número es igual a:\n{octal}(8)")
    else:
        octal = "0(8)"
        print(f"Su número es igual a:\n{octal}")
        
        
#Convertir Decimales a Hexadecimales 

def decimal_a_hexadecimal (numero_decimal):
    hexadecimal = "" 
  
    if numero_decimal != 0:   
        while numero_decimal > 0: 
             residuo = numero_decimal % 16 
             numero_decimal = numero_decimal // 16 
             if residuo == 10: 
                 residuo = "A" 
             elif residuo == 11: 
                 residuo = "B" 
             elif residuo == 12: 
                 residuo = "C" 
             elif residuo == 13: 
                 residuo = "D" 
             elif residuo == 14: 
                 residuo = "E" 
             elif residuo == 15: 
                 residuo = "F" 
             hexadecimal = str(residuo) + hexadecimal 
        print(f"\nSu número es igual a:\n{hexadecimal}(16)")
    else:
         hexadecimal = "0(16)"
         print(f"Su número es igual a:\n{hexadecimal}")


#Calculadora clásica 

def calculadora_clasica(): 
     operacion = "" 
     cuenta_total = "" 
     #cuenta_total mostrará toda la cuenta realizada al final 
     print ("\nUsted a seleccionado la calculadora clásica.") 
     resultado = float(input("Ingrese valor inicial: ")) 
     #Antes de inicar el bucle, se pide un valor inicial que no tendria problema en ser ingresado en la variable "resultado". 
     cuenta_total = (f"{resultado}") 
     while operacion != "=": 
         operacion = input("Ingrese operación (+, -, *, /) o '=' para terminar:\n")
         #Si no ingresa ninguna de las 5 salidas posibles, se vuelve a preguntar lo mismo. 
         if operacion == "+": 
             num = float(input("Ingrese número a sumar:  ")) 
             resultado += num 
             cuenta_total += (f" + {num}") 
             print(f"\nEl resultado hasta ahora es: {resultado}")
         if operacion == "-": 
             num = float(input("Ingrese número a restar:  ")) 
             resultado -= num 
             cuenta_total += (f" - {num}") 
             print(f"\nEl resultado hasta ahora es: {resultado}")
         if operacion == "/": 
             num = float(input("Ingrese número a dividir:  ")) 
             resultado /= num 
             cuenta_total += (f" / {num}") 
             print(f"\nEl resultado hasta ahora es: {resultado}")
         if operacion == "*": 
             num = float(input("Ingrese número a multiplicar:  ")) 
             resultado *= num 
             cuenta_total += (f" * {num}") 
             print(f"\nEl resultado hasta ahora es: {resultado}")
     cuenta_total += (f" = {resultado}") 
     print (f"\nUsted a realizado la siguiente cuenta: \n{cuenta_total}\nEl resultado final es: {resultado}") 
  

#Sumar fracciones

def sumas(num, den): 
     global op 
     global resultadoD 
     global resultadoN 
  
     while op != "=": 
         den = 0 
         while den == 0: 
             num = int(input("Ingrese numerador  \n")) 
             den = int(input("Ingrese denominador  \n")) 
         resultadoN = num * resultadoD + resultadoN * den 
         resultadoD = resultadoD * den 
         op = str(input("Ingrese = para mostrar el resultado, o apriete cualquier cosa para seguir sumando")) 
         mcd(resultadoN, resultadoD) 
  
  
#Restar fracciones

def restas(num, den): 
    global resultadoD 
    global resultadoN 
    global op 
    while op != "=": 
        den = 0 
        while den == 0: 
            num = int(input("Ingrese numerador \n")) 
            den = int(input("Ingrese denominador \n")) 
        resultadoN = num * resultadoD - resultadoN * den 
        resultadoD = resultadoD * den 
        op = str(input("Ingrese = para mostrar el resultado, o apriete cualquier cosa para seguir sumando")) 
        mcd(resultadoN, resultadoD) 
  
  
#Multiplicar y dividir fracciones

def dym(num, den): 
    den = 0 
    global op 
    global resultadoD 
    global resultadoN 
    global l
  
    while den == 0: 
        num = int(input("Ingrese numerador  \n")) 
        den = int(input("Ingrese denominador  \n")) 
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
  

#Conseguir el máximo común divisor/simplificar fraccciones

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
  

#Menú de calculadora de fracciones 

def menu_de_fracciones():
    global op
    global resultadoD
    global resultadoN
    global l
    while op != "=": 
        while resultadoD == 0: 
            resultadoN = int(input("\nIngrese numerador  \n")) 
            resultadoD = int(input("Ingrese denominador  \n")) 
        print("Ingrese...") 
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
            
    op = ""
    resultadoD = 0
    resultadoN = 1
    l = 0
    
    
#Menú de conversión numérica

def menu_de_conversion():
    numero_decimal = -1
    while numero_decimal < 0:
        numero_decimal = int(input("\nIngrese el número que desea convertir (solo enteros positivos):\n"))
    conversión = input("Ingrese el tipo de conversión que desea realizar (Bin, Hex, Oct):\n")
   
    if conversión.lower() == "bin":
        decimal_a_binario(numero_decimal)
        #convierte a binario y vuelve al menú de selección 
    elif conversión.lower() == "hex":
        decimal_a_hexadecimal(numero_decimal)
        #convierte a Hexadecimal y vuelve al menú de selección 
    elif conversión.lower() == "oct":
        decimal_a_octal(numero_decimal)
        #convierte a octal y vuelve al menú de selección 
    else:
        print ("\nOpción inválida")    
    
  
    
#Menú principal 
 
iniciar = "" 
cual = 0 
#La variable cual sirve para que la persona elija qué calculadora utilizar o si desea apagar la calculadora. 
try:
    while iniciar != "on": 
        iniciar  = input("Ingrese 'On' para iniciar calculadora: \n") 
        iniciar = iniciar.lower() 
        #Mientras no se ingrese On, el programa seguirá preguntando si desea iniciar la calculadora. 
    print ("\nSe ha iniciado la calculadora. ¡Bienvenido!") 
    while cual != 4: 
        print("\nSeleccione una opción:")
        print("1: Calculadora clásica")
        print("2: Calculadora de fracciones")
        print("3: Conversión numérica")
        print("4: Salir")
        cual = int(input())
        if cual == 1: 
            try:
                calculadora_clasica() 
            except ZeroDivisionError:
                print ("\nNo se puede dividir por 0")
            except ValueError:
                print ("\nValor inválido")
        elif cual == 2: 
            try:
                menu_de_fracciones() 
            except ValueError:
                print("\nSolo pueden seleccionarse números enteros")
        elif cual == 3: 
            try:
                menu_de_conversion() 
            except ValueError:
                print("\nSolo acepta números enteros")
                
    print("\n\nHa seleccionado apagar la calculadora. \nMuchas gracias.") 
except ValueError:
    print("Opción inválida")

      
# Sandy Pérez, Martín Aburto, Emmanuel Bertín

