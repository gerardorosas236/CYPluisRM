print("Programa Para Calcular El Area De un Tiangulo")
L1 = float(input("Ingresa el Valor del Primer Lado Del Triangulo: "))
L2 = float(input("Ingresa el Valor del Segundo Lado Del Triangulo: "))
L3 = float(input("Ingresa el Valor del Tercer Lado Del Triangulo: "))
S = (L1 + L2 + L3)/2
AREA = (S * (S-L1) * (S-L2) * (S-L3)) ** 0.5
print(f"El Area Del Triangulo Es: {AREA}")
