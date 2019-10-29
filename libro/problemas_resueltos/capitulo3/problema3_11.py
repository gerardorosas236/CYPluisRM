CAN1=0
CAN2=0
CAN3=0
CAN4=0
VOTO=int(input("Ingrese su voto por el candidato de su eleccion: "))
while (VOTO!=0):
    if VOTO==1:
        CAN1=CAN1+1
    elif VOTO==2:
        CAN2=CAN2+1
    elif VOTO==3:
        CAN3=CAN3+1
    elif CAN==4:
        CAN4=CAN4+1
    VOTO=int(input("Ingrese su voto por el candidato de su eleccion: "))
SUMV=(CAN1+CAN2+CAN3+CAN4)
POR1=(CAN1/SUMV)*100
POR2=(CAN2/SUMV)*100
POR3=(CAN3/SUMV)*100
POR4=(CAN4/SUMV)*100
print(f"VOTO CANDIDATO 1 {CAN1} PORCENTAJE OBTENIDO {POR1}")
print(f"VOTO CANDIDATO 2 {CAN2} PORCENTAJE OBTENIDO {POR2}")
print(f"VOTO CANDIDATO 3 {CAN3} PORCENTAJE OBTENIDO {POR3}")
print(f"VOTO CANDIDATO 4 {CAN4} PORCENTAJE OBTENIDO {POR4}")
print(f"CANTIDAD DE VOTANTES {SUMV}")
