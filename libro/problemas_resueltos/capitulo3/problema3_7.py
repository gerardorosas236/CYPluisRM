N=int(input("Ingrese el numero de ventas: "))
MED=0
CHI=0
GRA=0
for i in range(0,N,1):
    V=float(input("Ingrese el monto de la compra: "))
    if V<=200:
        CHI+=1
    elif V<400:
        MED+=1
    else:
        GRA+=1
print(f"Ventas menores o iguales a 200: {CHI}")
print(f"Ventas mayores a 200 y menores a 400: {MED}")
print(f"Ventas mayores a 400 {GRA}")
