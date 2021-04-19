print('Programa que simula un sistema de validacion de datos en una plataforma digital')

import os

USER = "cristian ortegon"
PASSWORD = 'c1234'

user = ''
password = ''

while USER != user or PASSWORD != password:
    os.system('cls')
    print ('             Validación de datos')
    user = input('Digite su Usuario: ')
    password = input('Digite su contraseña: ')

    if USER != user or PASSWORD != password:
        print('Credenciales incorrectas')
        print('Intenta de nuevo')
        input('Presiona enter para continuar...')
else:
    print('Bienvenido Cristian')

input('buen día...')
