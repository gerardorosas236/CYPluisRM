print("Programa Para Calcular El Resultado De Una Ecuacion De Segundo Grado Utilizando Formula General")
A = float(input("Ingrese al valor de A: "))
B = float(input("Ingrese al valor de B: "))
C = float(input("Ingrese al valor de C: "))
DIS = B**2-4*A*C
if DIS>=0:
    X1 = ((-B)+DIS**0.5)/(2*A)
    X2 = ((-B)-DIS**0.5)/(2*A)
    print(f"El Valor de X1 es: {X1}")
    print(f"El Valor de X2 es: {X2}")
print("Fin Del Programa....")


