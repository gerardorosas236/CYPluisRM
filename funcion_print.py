# Print tiene 4 formas de uso
"""
1.- con comas
2.- con signo '+'
3.- con la funcion format()
4.- es con una variante de format()
"""
# con comas , concatenar agregando un espaio y haciendo casting de tipo
edad=10
nombre="Juan"
estatura=1.67
print (nombre, edad, estatura)
# con '+' hace lo mismo pero no realiza el casting automatico
print (nombre + str(edad) + str(estatura))

# funcion format()
print("nombre: {} edad: {} ".format(nombre,edad))

# con una variante de format() simplificada
print (f"nombre: {nombre} \nedad: {edad} ")
