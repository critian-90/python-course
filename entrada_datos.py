print ("Calculadora simple")

print ("\nEscoge del siguiente menú la operación que deseas realizar")

print ("\nSi deseas realizar una'SUMA' digita el número 1")
print ("Si deseas realizar una'RESTA' digita el número 2")
print ("Si deseas realizar una'MULTIPLICACION' digita el número 3")
print ("Si deseas realizar una'DIVISION' digita el número 4")

opcion = int(input("\nPor favor digita la opción deseada: "))

num_uno = int(input("Ingresa el primer número: "))
num_dos = int(input("Ingresa el segundo número: "))


if opcion == 1 :
    resultado = (num_uno + num_dos)
    print ("El resultado de la suma es: " , resultado)
elif opcion == 2 :
    resultado = (num_uno - num_dos)
    print ("El resultado de la resta es: " , resultado)
elif opcion == 3 :
    resultado = (num_uno * num_dos)
    print ("El resultado de la multiplicacion es: " , resultado)
elif opcion == 4 :
    resultado = (num_uno / num_dos)
    print ("El resultado de la division es: " , resultado)
else:
    print ("Opcion no valida")

print ("Fin del programa")

