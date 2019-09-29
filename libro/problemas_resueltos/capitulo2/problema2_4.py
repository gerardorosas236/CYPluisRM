MAT = int(input("Ingresa Tu Matricula De Alumno: "))
CAL1 = float(input("Ingresa Tu Primera Calificacion: "))
CAL2 = float(input("Ingresa Tu Segunda Calificacion: "))
CAL3 = float(input("Ingresa Tu Tercera Calificacion: "))
CAL4 = float(input("Ingresa Tu Cuarta Calificacion: "))
CAL5 = float(input("Ingresa Tu Quinta Calificacion: "))
PROM = (CAL1+CAL2+CAL3+CAL4+CAL5)/5
if PROM>=6:
    print(f"Matricula: {MAT} Obtuvo El Promedio De: {PROM}, Aprobado")
else:
    print(f"Matricula: {MAT} Obtuvo El Promedio De: {PROM}, No Aprobado")

