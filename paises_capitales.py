MEXICO = 1
URUGUAY = 2
COLOMBIA = 3
ARGENTINA = 4
ECUADOR = 53
PERU = 6

print (' Programa para conocer la capital del pais seleccionado del siguiente Menu')


print ('''          Capitales de América
1) México
2) Uruguay
3) Colombia
4) Argentina
5) Ecuador
6) Perú''')

opc = int(input('\nSelecciona una opción: '))

if opc == MEXICO :
    print('Tiene como capital ciúdad de mexico')
elif opc == URUGUAY :
    print ('Tiene como capital a Motevideo')
elif opc == COLOMBIA :
    print ('Tiene como capital a Bogota')
elif opc == ARGENTINA :
    print (' Tiene como capital Buenos Aires')
elif opc == ECUADOR :
    print (' Tiene como capital a Quito')
elif opc == PERU :
    print (' Tiene como capital A Lima')
else :
    print ('Opción no valida')

print ('Fin del programa')
