print ( '''juego de preguntas y respuestas,
si el usuario contesta correctamente una pregunta puede continuar con la siguiente
en caso contrario el juego finalizara''')

print('Bienvenid@ pongamos a prueba tus conocimientos sobre la Familia')
respuesta = int(input('¿Cuantos años tiene Cristian Ortegon?: '))
if respuesta == 30 :
    print ('¡Correcto!')
    respuesta = int(input('¿Cual es el día de nacimiento de Evangeliene?: '))
    if respuesta == 15 :
        print ('¡Correcto!')
        respuesta = input('¿Verde por fuera y roja por dentro... y con bailarinas en el centro?: ')
        if respuesta == 'sandia':
            print ('Correcto felicitaciones')
        else :
            print ('Respuesta incorrecta, es una fruta y comienza por S')

    else:
        print ('Respuesta incorrecta Ecoooo ')
else :
    print ('Respuesta incorrecta que tristeza')

print ('Fin del programa')

