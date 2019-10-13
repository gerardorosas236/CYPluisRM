TIPOENF = int(input("Ingrese el tipo de enfermedad que tiene: "))
EDAD = int(input("Ingrese su edad: "))
DIAS = int(input("Ingrese el numero de dias que estubo hospitalizado: "))
if TIPOENF==1:
    COSTOT=DIAS*25
elif  TIPOENF==2:
    COSTOT=DIAS*16
elif TIPOENF==3:
    COSTOT=DIAS*20
elif TIPOENF==4:
    COSTOT=DIAS*32
if EDAD>=14 and EDAD<=22:
    COSTOT=COSTOT*1.10
else:
    print(f"El Total A Pagar Es De: ${COSTOT}")
