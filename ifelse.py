edad = int( input("Dame Tu Edad: "))
INE = bool(  int(input("Tienes INE (0 NO / 1 SI): ")))
if edad >= 18 and INE == True:
    print("Eres Mayor De Edad")
    print("Puedes entrar al Bar")
else:
    print("Eres Menor de Edad")
    print("Puedes ir a Jugar LOL")
print("Fin del Programa.....")
