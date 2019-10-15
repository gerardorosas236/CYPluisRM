SUE = float(input("Ingrese Su Sueldo: "))
CATE = int(input("Ingrese La Categoria A la Que Pertenece: "))
HE = int(input("Ingrese Sus Horas Extras Trabajadas: "))
if CATE==1:
    PHE=30
elif CATE==2:
    PHE=38
elif CATE==3:
    PHE=50
elif CATE==4:
    PHE=70
else:
    PHE=0
if HE>30:
    NSUE=SUE+30*PHE
    print(f"Su Sueldo Total Es De: ${NSUE}")
else:
    NSUE=SUE+HE*PHE
    print(f"Su Sueldo Total Es De: ${NSUE}")
