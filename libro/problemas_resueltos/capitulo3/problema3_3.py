SERIE=0
N=int(input("Ingrese un numero entero: "))
BAND=True
for I in range(1,N+1,1):
    if BAND==True:
        SERIE=SERIE+1/I
        BAND=False
    else:
        SERIE=SERIE -1/I
        BAND=True
print(BAND,SERIE)
