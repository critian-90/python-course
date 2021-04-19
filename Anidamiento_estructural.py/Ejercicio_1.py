def esmoneda(cripto): #recibe la moneda y verifica que esta se encuentre la lista de criptos
    criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]
    if cripto in criptos: #si la moneda esta  retorna true y si no esta retorna false
        return True
    else:
        return False



numero = 0
valor = 0.0

while numero <= 2 :
    cripto = input('digite el nombre de la criptomoneda: ')
    btccant =float(input(f'Ingrese la cantidad de {cripto} que posee:  '))
    btccotz =float(input(f'Ingrese la cotizacion en USD DE {cripto} : '))
    numero = numero +1
    valor = valor + (btccant * btccotz)
    print (f'Usted posee un total de {valor} dolares americanos' )
    
else :
    print ('Opcion no valida')


       

print ('Fin del programa')