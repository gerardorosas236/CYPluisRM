print("Programa Que Calcula El Area y Volumen De Un Cilindro")
RADIO = float(input("Introduce el valor del Radio: "))
ALTU = float(input("Introduce el Valor de la Altura: "))
VOL = 3.141592 * (RADIO ** 2) * ALTU
ARE = 2 * 3.141592 * RADIO * ALTU
print(f"El Volumen del Cilindro es: {VOL}")
print(f"El Área del Cilindro es: {ARE}") 
