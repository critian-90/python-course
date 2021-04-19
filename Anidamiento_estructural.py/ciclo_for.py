''' repetitiva_desde_1.py
script e python que muestre los números enteros
 desde el 0 hasta el 13 usando un ciclo for
'''
print ('Programa que muestra los numeros del 0 al 13 con for')

for numero in range(14):
    print (f'{numero}')

print('Fin del programa')

print('Imprima los números pares desde el 2 al 20')

print('\nMetodo 1', sep=(''))
for par in range (1, 11):
    print (f'{par*2}')
print('*'*20)
print('\nmetodo 2')

for par in range(2, 21):
    if par % 2 == 0:
        print (f'par: {par}')

print('Fin del segundo programa')

print('*'*20)
print('\nmetodo 2')

for par in range(2, 21, 2):
    print('Los números par son:' + str(par))



