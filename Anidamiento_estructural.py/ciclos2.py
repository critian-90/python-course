print ('''\nPrograma que suma valores pares y multiplique valores impares
mientras el usuario no ingrese un 0. Se deberá utilizar la estructura repetitiva "while" para solicitar
 al usuario un número y dependiendo del número lo suma o lo multiplica.''')

suma = 0
multiplicacion = 1
numero = -1

while numero != 0 :
    numero = int(input('\nIngrese un número (0 para salir): '))
    if numero % 2 == 0:
        suma = suma + numero
    else :
        multiplicacion = multiplicacion * numero

    print (f'suma: {suma}')
    print (f'multiplicacion: {multiplicacion}')

print ('Fin del programa')