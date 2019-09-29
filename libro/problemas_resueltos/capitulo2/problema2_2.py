print("Programa que dados como datos los valores de P y Q, determinen la siguiente expresión: P^3+q^4-2*P<680")
P = int(input("Ingresa el valor de P: "))
Q = int(input("Ingresa el valor de Q: "))
EXP = P**3+Q**4-2*P**2
if EXP<680:
    print(f"{P}")
    print(f"{Q}")
print("Fin Del Programa....")

