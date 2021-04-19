# Se slicita a uuario calificación y cantidad de asistencias al curso

MIN_CALF = 60
MIN_ASIS = 20

print ("Por favor ingrese los siguientes datos: ")

calificacion = float(input("Calificación: "))
asistencia = float(input("Cantidad de asistencia al curso: "))

if calificacion >= MIN_CALF and asistencia >= MIN_ASIS :
    print ("Felicitaciones aprobaste el curso")
elif calificacion >= MIN_CALF and asistencia < MIN_ASIS :
    print ("Tú calificacón es aprobatoria pero pierdes por inasistencia")
elif calificacion < MIN_CALF and asistencia >= MIN_ASIS :
    print ("Tú calificación es insuficiente a pesar de aprobar asitencia")
else:
    print ("Lo sentimos haz reprobado el curso")

print ("Fin del programa")
