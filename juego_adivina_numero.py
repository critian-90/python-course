# Solicite al usuario intente adivinar un numero entre 1 y 10.

import random

secreto = random.randint(1, 10)
print ('Acabo de generar un número secreto entre 1 y 10')
usuario = int(input('¿Cual crees que sea mi número?: '))

if usuario == secreto :
    print('Felicitaciones acertaste mi número secreto es: ' + str(secreto))
else:
    print ('Lo siento el número secreto es: '+ str(secreto))

print ('Fin del programa')

# Simulación de validación de una plataforma digital

USER = ("cristian")
PASSWORD = ("1234cris")

print("Por Favor ingresa los siguientes datos: ")
user = input("Usuario: ")
password = input("Contraseña: ")

if user == USER and password == PASSWORD :
    print ("Ingreso autorizado")
else:
    print ("Datos incorrectos")

