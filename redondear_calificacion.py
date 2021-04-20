print ("""Sistema para calcular la calificación de un estudiante y redondear la suma a multiplo de 10 si le faltan 4 decimas
para serlo""")

calf_mat = (float(input("¿Por favor digite su calificación en matematicas?: ")))
calf_bio = (float(input("¿Por favor digite su calificación en biologia?: ")))
calf_qui = (float(input("¿Por favor digite su calificación en quimica?: ")))

calificacion = (calf_bio + calf_mat + calf_qui) / 3
residuo = (calificacion % 10)
mensaje = ('Tú calificación no amerita redondeo')

print ("Su calificación es: " + str(calificacion))


if 0 <= calificacion <= 100 and residuo >= 6 :
    calificacion = calificacion + (10 - residuo)
    print ("Se ha redondeado tu calificación a: " + str(calificacion))

print (mensaje)
    
print ("Fin del programa")