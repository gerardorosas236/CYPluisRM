SUE = float(input("Ingrese Su Sueldo: "))
if SUE<1000:
    print("Su Sueldo es inferior a $1000, por lo tanto tiene un aumento del 15%")
    NSUE1 = SUE * 1.15
    print(f"Su Sueldo total con el aumento del 15% es de ${NSUE1}")
else:
    print("Su Sueldo es superior a $1000, por lo tanto tiene un aumento del 12%")
    NSUE2 = SUE * 1.12
    print(f"Su Sueldo total con el aumento del 12% es de ${NSUE2}")
print("Fin Del Programa....")
