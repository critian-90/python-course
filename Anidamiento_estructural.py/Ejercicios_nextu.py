import os
cripto1 = int(input('Digite el valor de la primera criptomoneda: '))
cripto2 = int(input('Digite el valor de la segunda criptomoneda: '))
cripto3 = int(input('Digite el valor de la tercer criptomoneda: '))

os.system('cls')
if cripto1 > cripto2 and cripto1 > cripto3:
    print (f' mayor {cripto1}')
    if cripto2 > cripto3 :
        print(f'medio {cripto2}')
        print(f'bajo {cripto3}')
elif cripto2 > cripto3 and cripto2 > cripto1:
    print (f' mayor {cripto2}')
    if cripto1 > cripto3:
        print(f'medio {cripto1}')
        print(f'bajo {cripto3}')
elif cripto3 > cripto2 and cripto3 > cripto1:
    print (f' mayor {cripto3}')
    cripto2 > cripto1 
    print(f'medio {cripto2}')
    print(f'bajo {cripto1}')

print ('Fin del programa')




