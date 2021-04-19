print ('************ Programa Calculadora *****************')

print ('\nSeñor usuario del siguiente menú de opciones seleccione la operacion a realizar')

SUMA = 1
RESTA = 2
MULTIPLICACION = 3
DIVISION = 4
DIVISION_ENTERA = 5
MODULO = 6
POTENCIA = 7

print('''                \nMenú de opciones   
1) Suma +
2) Resta -
3) Multiplicación *
4) División /
5) División entera //
6) Modulo o resto %
7) Potencia **
''')

opc = int(input('Por favor ingrese el número de su opción: '))

if opc == SUMA :
    num_uno = int(input('\nIngrese el primer número a sumar: '))
    num_dos = int(input('Ingrese el segundo número a sumar: '))
    resultado = (num_uno + num_dos)
    print ('El resultado de la suma es: ' + str(resultado))
elif opc == RESTA :
    num_uno = int(input('\nIngrese el primer número a restar: '))
    num_dos = int(input('Ingrese el segundo número a restar: '))
    resultado = (num_uno - num_dos)
    print ('El resultado de la resta es: ' + str(resultado))
elif opc == MULTIPLICACION :
    num_uno = int(input('\nIngrese el primer número a multiplicar: '))
    num_dos = int(input('Ingrese el segundo número a multiplicar: '))
    resultado = (num_uno * num_dos)
    print ('El resultado de la multiplicación es: ' + str(resultado))
elif opc == DIVISION :
    num_uno = int(input('\nIngrese el primer número a dividir: '))
    num_dos = int(input('Ingrese el segundo número a dividir: '))
    if num_dos == 0 :
        print ('Error matematico, Fin del programa')
    resultado = (num_uno / num_dos)
    print ('El resultado de la División es: ' + str(resultado))
elif opc == DIVISION_ENTERA :
    num_uno = int(input('\nIngrese el primer número a dividir: '))
    num_dos = int(input('Ingrese el segundo número a dividir: '))
    if num_dos == 0 :
        print ('Error matematico, Fin del programa')
    resultado = (num_uno // num_dos)
    print ('El resultado de la División es: ' + str(resultado))
elif opc == MODULO :
    num_uno = int(input('\nIngrese el primer número: '))
    num_dos = int(input('Ingrese el segundo número : '))
    if num_dos == 0 :
        print ('Error matematico, Fin del programa')
    resultado = (num_uno % num_dos)
    print ('El resultado del resto de la división es: ' + str(resultado))
elif opc == POTENCIA :
    num_uno = int(input('\nIngrese el primer número: '))
    num_dos = int(input('Ingrese el segundo número : '))
    resultado = (num_uno ** num_dos)
    print ('El resultado de elevar el número a la potencia es: ' + str(resultado))
else :
    print ('Opcion no valida')

print ('Fin del programa')
