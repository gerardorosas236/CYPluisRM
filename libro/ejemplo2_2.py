SUE = float(input("Ingrese su sueldo: "))
if SUE<1000:
    print("Su sueldo es inferior a $1000, por lo tanto tiene un aumento del 15%")
    AUM = SUE * 0.15
    NSUE = SUE + AUM
    print(f"Su sueldo total con el 15% de aumento es {NSUE}")
print("Fin Del Programa....")
