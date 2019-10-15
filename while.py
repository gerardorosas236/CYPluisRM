otra = True
suma= 0.0
cont=0
while(otra==True):
    cal=float(input("Ingresa Calificacion: "))
    cont+=1
    suma=suma+cal
    otra= bool(int(input("Hay mas alumnos (0 No, 1 Si):")))
print("suma",suma)
print("Promedio: ",suma/cont)
