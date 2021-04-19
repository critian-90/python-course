print('''Juego de adivinar un número, pero esta vez en modo competitivo.
 La computadora deberá generar un número aleatorio entre 1 y 100, 
tanto el usuario como la computadora deberán intentar adivinar dicho número. 
Para que el juego sea retador el jugador máquina deberá ser " inteligente" y competir para ganar.
El juego se realizará por turnos, primero la máquina y después el usuario
 y por cada intento la computadora responderá si el número es mayor 
o menor que el secreto.''')

import os
import random

inferior = 1
superior = 100

secreto = random.randint(1, 100)

usuario = -1
maquina = -1



while usuario != secreto and maquina != secreto:
    os.system('cls')
    print ('maquina ¿ Cual crees que es el número secreto')
    maquina = random.randint(inferior, superior)
    print (f'Mi valor es: {maquina}')
    if maquina < secreto:
        print('El número es menor')
        inferior = maquina + 1
    elif usuario > secreto :
        print('El número es mayor')
        superior = maquina - 1
    else:
        print ('Felicidades maquina acertaste')
    if maquina != secreto:
        usuario = int(input('Usuario ¿Cual crees que es el número secreto: '))
        if usuario < secreto :
            print('El número es menor')
            if usuario > inferior:
                inferior = usuario + 1
        elif usuario > secreto:
            print('El número es mayor')
            if usuario < inferior:
                    inferior = usuario - 1
        else:
            print ('Felicidades usuario acertaste')
    input('presiona enter para continuar..')

print ('Fin del programa')


