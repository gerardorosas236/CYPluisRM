print("La Tienda Aplica Los Siguientes Descuentos: ")
print("Si El Monto Es Menor Que $500 , No Hay Descuento.")
print("Si El Monto Esta Comprendido Entre $500 y $1,000 , Descuento Del 5%.")
print("Si El Monto Esta Comprendido Entre $1,000 y $7,000 , Descuento Del 11%.")
print("Si El Monto Esta Comprendido Entre $7,000 y $15,000 , Descuento Del 18%.")
print("Si El Monto Es Mayor a $15,000 , Descuento Del 25%.")
COMPRA = float(input("Ingrese El Monto Total De Su Compra: "))
if COMPRA<500:
    PAGAR = COMPRA
    print(f"El Total A Pagar Aplicando el Descuento es: ${PAGAR}")
else:
    if COMPRA<=1000:
        PAGAR = COMPRA -(COMPRA*0.05)
        print(f"El Total A Pagar Aplicando el Descuento es: ${PAGAR}")
    else:
        if COMPRA<=7000:
            PAGAR = COMPRA -(COMPRA*0.11)
            print(f"El Total A Pagar Aplicando el Descuento es: ${PAGAR}")
        else:
            if COMPRA<=15000:
                PAGAR = COMPRA -(COMPRA*0.18)
                print(f"El Total A Pagar Aplicando el Descuento es: ${PAGAR}")
            else:
                PAGAR = COMPRA -(COMPRA*0.25)
                print(f"El Total A Pagar Aplicando el Descuento es: ${PAGAR}")
print("Fin Del Programa....")



