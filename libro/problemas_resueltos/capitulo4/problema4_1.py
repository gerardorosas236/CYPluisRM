N=int(input("Ingrese el numero de elementos del arreglo: "))
VEC=[]
if N>=1 and N<=500:
    #logica
    for i in range(0,N,1):
        VEC.append(int(input("Ingresa valor: ")))
    VEC.sort()
    print("Lista de numeros sin repeticiones")
    i=0
    while i<=N-1:
        print(VEC[i])
        repet=(VEC[i])
        while i<=N-1 and repet==VEC[i]:
            i+=1
else:
    print("el numero de arreglos es incorrecto")

