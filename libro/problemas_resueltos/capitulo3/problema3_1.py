SUMPAR=0
SUMIMP=0
CUEPAR=0
for I in range(1,271,1):
    NUM=int(input("Ingrese un Numero entero: "))
if NUM!=0:
    if (-1**NUM)>0:
        SUMPAR+=NUM
        CUEPAR+=1
    else:
        SUMIMP+=NUM
PROPAR=SUMPAR/CUEPAR
print(f"El promedio de los pares es {PROPAR} y la suma de los impares es {SUMIMP}")
