#Diccionarios['llave':'valor']
alumno={"num_cta":"2317089327",
        "nombre":
        "jose",
        "paterno":"perez",
        "semestre": 1,
        "promedio":0.0,
        "materias":["CYP","algebra","calculo","geometria","IntroICO"],
        'regular':True,
        'lagrimas_por_examen':5,
        'direccion':{
            'calle':'rancho seco',
            'numero':'69',
            'colonia':'impulsora',
            'cp':'07570',
            'municipio':'neza',
            'estado':{
                'id':15,
                'nombre':'Estado De Mexico',
                'corto':'EDOMEX',
                }
            }
        }
print(alumno['materias'][1].upper())
print(alumno['nombre'])
print(alumno)
print(alumno['paterno'][1])
print(alumno['direccion']['cp'])
print(alumno['direccion']['estado']['corto'])
print(alumno['direccion']['estado']['nombre'][10::1].upper())
alumno['lagrimas_por_examen']=10
print(alumno)

mi_lista=[['a','b'],['c',10],['d',True]]
diccionario=dict(mi_lista)
print(diccionario)

#Son mutables
alumno['cursa_ingles']=True
print(alumno)
#Funcion keys
llaves=alumno.keys()
print(llaves)
for llave in llaves:
    print("---------------------")
    print(llave)
    print(".....................")
    print(alumno[llave])
    print("---------------------")
    
#Funcion value
for val in alumno.values():
    print(".......")
    print(val)
    print(".......")
    
