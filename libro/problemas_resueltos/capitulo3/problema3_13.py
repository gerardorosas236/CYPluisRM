ARSU=0
ARNO=0
MERSU=50000
MES=0
ARCE=0
for i in range(1,13,1):
    print(f"mes {i}: ")
    RNO=int(input("Promedio de lluvias del mes zona norte: "))
    RCE=int(input("Promedio de lluvias del mes zona centro: "))
    RSU=int(input("Promedio de lluvias del mes zona sur: "))

    ARNO=ARNO+RNO
    ARCE=ARCE+RCE
    ARSU=ARSU+RSU

    if RSU<MERSU:
        MERSU=RSU
        MES=1
PRORCE=ARCE/12
print(f"Promedio region centro: {PRORCE}")
print(f"Mes con menor lluvia region sur: {MES}")
print(f"Registro del mes: {MERSU}")

if ARNO>ARCE:
    if ARNO>ARSU:
        print("La region con mayor lluvia es la region norte")
    else:
        print("La region con mayor lluvia es la region sur")
else:
    if ARCE>ARSU:
        print("La region con mayor lluvia es la region centro")
    else:
        print("La region con mayor lluvia es la region sur")

print("Fin Del Programa....")
