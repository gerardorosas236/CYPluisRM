print("Programa Que Determina Si Un Numero Es Positivo, Nulo, o Negativo")
NUM = int(input("Ingresa Un Numero Entero: "))
if NUM>0:
    print(f"El Numero {NUM} es Positivo")
else:
    if NUM==0:
        print(f"El Numero {NUM} es Nulo")
    else:
        print(f"El Numero {NUM} es Negativo")
print("Fin Del Programa....")
