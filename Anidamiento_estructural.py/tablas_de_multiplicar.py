import os

print ('''tabla de multiplicar del 1 al 10''')

for numero in range(1, 11):
    os.system('cls')
    print(f'                    Tabla de multiplicar del {numero}')
    for multiplo in range(1, 11):
        print (f'{numero} X {multiplo} = {numero * multiplo}')
    input ('presiona enter para continuar...')

print ('Fin del programa')