print("Programa Que Determina Si Tres Numeros Enteros Estan En Orden Creciente")
A = int(input("Ingresa el valor del primer numero: "))
B = int(input("Ingresa el valor del segundo numero: "))
C = int(input("Ingresa el valor del tercer numero: "))
if A<B:
    if B<C:
        print(f"Los Numeros {A} {B} {C}, estan En Orden Creciente")
    else:
        print(f"Los Numeros {A} {B} {C}, no Estan En Orden Creciente")
else:
    print(f"Los Numeros {A} {B} {C}, no Estan En Orden Creciente")

print("Fin Del Programa....")
