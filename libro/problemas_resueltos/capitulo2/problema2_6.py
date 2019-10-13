print("Programa Que Determina Si Un Numero Es Par, Impar, o Nulo")
A = int(input("Ingresa Un Numero Entero: "))
if A==0:
    print(f"El Numero {A} es Nulo")
else:
    if (-1)**A>0:
        print(f"El Numero {A} es Par")
    else:
        print(f"El Numero {A} es Impar")
print("Fin Del Programa....")
