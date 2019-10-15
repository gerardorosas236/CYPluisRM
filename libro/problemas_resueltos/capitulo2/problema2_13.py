MAT = int(input("Ingresa Tu Matricula De Alumno: "))
CARR = str(input("Ingresa La Carrera En La Que Estas Inscrito: "))
SEM = int(input("Ingresa El Semestre En el Que Estas Inscrito: "))
PROM = float(input("Ingresa Tu Promedio: "))
if CARR=="economia":
    if SEM>=6 and PROM>=8.8:
        print(f"Matricula {MAT}, Carrera {CARR}, Aceptado")
if CARR=="computacion":
        if SEM>6 and PROM>8.5:
            print(f"Matricula {MAT}, Carrera {CARR}, Aceptado")
if CARR=="contabilidad" or "administracion":
    if SEM>5 and PROM>8.5:
        print(f"Matricula {MAT}, Carrera {CARR}, Aceptado")












