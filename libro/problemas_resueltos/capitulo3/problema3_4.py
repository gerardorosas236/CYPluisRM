NOM=0
SUE=float(input("Ingrese su sueldo: "))
while SUE!=-1:
    if SUE<1000:
        NSUE=SUE*1.15
    else:
        NSUE=SUE*1.12
        NOM=N0M+NSUE
    print(f"Su nuevo sueldo es: {NSUE}")
    SUE=float(input("Ingresa tu sueldo: "))
print(f"El sueldo total de todos los trabajadores es: {NOM}")

