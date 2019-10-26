N=int(input("Ingresa el numero: "))
MAY=-100000
MEN=100000
for i in range(0,N,1):
    NUM=int(input("Ingrese un numero entero: "))
    if NUM>MAY:
        MAY=NUM
        if NUM<MEN:
            MEN=NUM
print(f"El maximo es {MAY} y el minimo es {MEN}")

