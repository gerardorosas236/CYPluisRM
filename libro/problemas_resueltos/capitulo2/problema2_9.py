PREBAS = float(input("Ingresa el precio Basico del producto: "))
if PREBAS>500:
    IMP = 20*0.30+(PREBAS-40)*0.50
else:
    if PREBAS>40:
        IMP = 20*0.30+(PREBAS-40)*0.40
    else: 
            if PREBAS>20:
                IMP = (PREBAS-20)*0.30
            else:
                 IMP=0
PRETOT = PREBAS+IMP
print(f"El Precio Basico Es De: ${PREBAS}, Aplicando El Descuento Es De: ${PRETOT}")

