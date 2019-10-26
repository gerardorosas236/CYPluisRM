BAND=True
SUMSER=0
I=2
while I<=1800:
    SUMSER+=I
    print(I)
    if BAND==True:
        BAND=False
        I+I+3
    else:
        BAND=True
        I=I+2
print(f"La suma total de los elementos de la serie es: {SUMSER}")

