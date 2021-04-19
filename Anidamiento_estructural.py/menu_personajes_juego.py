print('''Menú con distintos personajes,
 si el usuario selecciona alguno, 
 se mostraran sus caracteristicas''')

import os

MAGO = 1
GUERRERO = 2
SACERDOTISA = 3
SALIR = 4

#bandera
continuar = True

while continuar:
    os.system('cls')
    print(f'''                   PERSONAJES
    {MAGO}) Mago
    {GUERRERO}) Guerrero
    {SACERDOTISA}) Sacerdotisa
    {SALIR}) Salir 
    ''')

    opc = int(input('Selecciona el número de tu personaje: '))

    if opc == MAGO:
        print('''
        Fuerza: 24
        Energía: 18
        Especial: 10
        ''')
    elif opc == GUERRERO:
        print('''
        Fuerza: 30
        Energía: 32
        Especial: 3
        ''')
    elif opc == SACERDOTISA:
        print('''
        Fuerza: 21
        Energía: 28
        Especial: 6
        ''')
    elif opc == SALIR:
        continuar = False
    else:
        print('Opción no valida')
    input('presiona enter para continuar')
input(' Nos vemos')

   
