A = int(input("Introduce un numero entero positivo: "))
B = int(input("Introduce un numero entero positivo: "))
C = int(input("Introduce un numero entero positivo: "))
if A>B:
    if A>C:
        if B>C:
            print(f"{A},{B},{C}")
        else: 
            print(f"{A},{B},{C}")
    else:
            print(f"{C},{A},{B}")
else:
    if B>C:
        if A>C:
            print(f"{B},{A},{C}")
        else:
            print(f"{B},{C},{A}")
    else:
        print(f"{C},{B},{A}")
print("Fin del Programa.....")
