#import modulos
#modulos.mi_print("Hola")

from modulos import *
import time
import sys
from asciistuff import Banner

mi_print("Hola De Nuevo")
otro_print("Otro print usado")
print (sumar(4 , 5))
print (restar(10 , 7))

for i in range (10,0,-1):
    print( i, "..." )
    time.sleep(1)
print("BOOOOOOM!!!!!")
    
print(Banner("\33[33mUniversidad Nacional Autonoma De Mexico"))
print(Banner("\33[34mFES Aragon"))
print(Banner("\33[32mRosas Mora Luis Gerardo"))
