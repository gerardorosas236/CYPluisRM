A = int(input("Introduce un valor entero positivo: "))
B = int(input("Introduce un valor entero positivo: "))
C = int(input("Introduce un valor entero positivo: "))
if A>B:
    if A>C:
        print(f"{A} es el numero mayor")
    elif A==C:
        print(f"{A}y {C} son los mayores")
    else:
        print(f"{C} es el mayor")
if A==B:
    if A>C:
        print(f"{A} Y {B} son mayores")
    else:
        if A==C:
            print(f"{A} {B} Y {C} son iguales")
        else:
            print(f"{C} es el mayor")
else:
    if B>C:
        print(f"{B} es el mayor")
    else:
        if B==C:
            print(f"{B} y {C} son los mayores")
        else: 
            print(f"{C} es el mayor")

print("Fin Del Programa...")



