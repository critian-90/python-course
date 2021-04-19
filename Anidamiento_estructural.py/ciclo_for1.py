import os
import time

for numero in range(3, -1, -1):
    os.system('cls')
    print(numero)
    time.sleep(1)

print('Se Muestra una cuenta regresiva')

print('*'*20)
print('''Tabla de multiplicar de un número ingresado por el usuario.
El usuario también podrá ingresar hasta
qué valor llegará la tabla de multiplicar.
''')

numero = int(input('¿De qué número deseas ver la tabla de multiplicar?: '))
limite = int(input('Hasta que múltiplo deseas ver?: '))
print(f'      Tabla del {numero}')
for multiplo in range(1, limite+1):
    print (f'{numero} X {multiplo} = {numero * multiplo}')