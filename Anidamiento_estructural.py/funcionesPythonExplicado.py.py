def esmoneda(cripto): #recibe la moneda y verifica que esta se encuentre la lista de criptos
    criptos = ["BTC","BCC","LTC","ETH","ETC","XRP"]
    if cripto in criptos: #si la moneda esta  retorna true y si no esta retorna false
        return True
    else:
        return False


def esnumero(numero): 
    return numero.replace('.','',1).isdigit()
#Listo, debes saber primero qué replace e isdigit son funciones de python.
#Lo que hace replace es reemplazar información en un string
#Lo que realiza isdigit es verificar que un string tenga solo dígitos o sea solo numeros, no puede tener ni comas, ni espacios, ni puntos, ni ningún otro carácter.
#Para este ejercicio en especifico se esta primero reemplazando la información en la variable cant.
#Como ves replace tiene 3 parámetros, que es el punto(.), después dos comillas sencillas que significa que no agregue nada ('') y después un 1
#El punto es el valor a reemplazar, y se va a reemplazar por nada que son las comillas y el uno hace referencia a un contador, o sea solo se va a hacer el remplazo una sola vez.


total=0
i=0
while (i < 3):
    cripto = input("Ingrese el nombre de la moneda: ") #solicitamos la moneda a validar
    if esmoneda(cripto):#valida si la moneda ingresada esta en la lista, si esta  seguimos pidiendo los datos
        i=i+1
        cant = "" #inicializamos cant en vacio para que se cumpla el while not de abajo
        while not esnumero(cant): #aqui seguira preguntando por la cantidad hasta que se cumpla que sea un numero valido
            cant = input("Indique la cantidad de "+cripto+":")
        cotiz="" #inicializamos cotiz en vacio para que se cumpla el while not de abajo
        while not esnumero(cotiz): #lo mismo que  con el while not de arriba, se pide el dato hast que cumpla las condiciones
            cotiz = input("Indique la cotización en USD de "+cripto+":")
        total = total + float(cant) * float(cotiz) #luego que se tiene todo se calcula el total
    else:
        print("Moneda invalida.") #si la moneda no esta en la lista arroja este mensaje
print("El tota en USD que tiene el usuario es de ",str(total)) # se imprime el resultado
