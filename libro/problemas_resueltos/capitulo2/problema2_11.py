print("Programa que calcula el costo de llamadas a largas distancias")
CLAVE = int(input("Ingresa La Clave De La Zona Geografica A La Que LLamo: "))
NUMIN = int(input("Ingresa La Duracion En Minutos De La LLamada Telefonica: "))
if CLAVE==12:
    COST = NUMIN*2
elif CLAVE==15:
    COST = NUMIN*2.2
elif CLAVE==18:
    COST = NUMIN*4.5
elif CLAVE==19:
    COST = NUMIN*3.5
elif CLAVE==23:
    COST = NUMIN*6
elif CLAVE==25:
    COST = NUMIN*6
elif CLAVE==29:
    COST = NUMIN*5
print(f"Costo Total De La LLamada: ${COST}")
