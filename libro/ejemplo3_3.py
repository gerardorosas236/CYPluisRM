CUECER=0
N=int(input("Ingresa Un Numero Entero Positivo: "))
for i in range(0,N,1):
    NUM=int(input("Ingresa Un Entero: "))
    if NUM==0:
        CUECER += 1
print(f"El Numero De Ceros Capturados Fue: {CUECER}")
