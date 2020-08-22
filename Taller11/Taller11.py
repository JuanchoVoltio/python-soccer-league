
import math

texto=("Indique a cuál figura le desea Calcular el área: \n"
       "Ingrese A para indicar círculo \n"
       "Ingrese B para indicar triángulo isósceles \n"
       "Ingrese C para indicar trapecio rectángulo \n"
       ">>>")

figura=input(texto)

if figura.upper()=="A":
    try:
        r=float(input("Ingrese el radio del círculo \n"
                ">>>"))
        area=math.pi*r**2
    except:
        try:
            print("Debe ingresar únicamente valores númericos")
            r=float(input("Ingrese el radio del círculo \n"
                        ">>>"))
            area=math.pi*r**2
        finally:
            print("Entiendo que no desea calcular ningún área \n"
                  "Hasta luego")
elif figura.upper()=="B":
    try:
        b=float(input("Ingrese la base del triángulo \n"
                ">>>"))
        h=float(input("Ingrese la altura del triángulo \n"
                ">>>"))
        area=b*h/2
    except:
        try:
            print("Debe ingresar únicamente valores númericos")
            b=float(input("Ingrese la base del triángulo \n"
                          ">>>"))
            h=float(input("Ingrese la altura del triángulo \n"
                          ">>>"))
            area=b*h/2
        finally:
            print("Entiendo que no desea calcular ningún área \n"
                  "Hasta luego")
elif figura.upper()=="C":
    try:
        b1=float(input("Ingrese la base menor del trapecio \n"
                       ">>>"))
        b2=float(input("Ingrese la base mayor del trapecio \n"
                       ">>>"))
        h=float(input("Ingrese la altura del trapecio \n"
                       ">>>"))
        area=(b1+b2)*h/2
    except:
        try:
            print("Debe ingresar únicamente valores númericos")
            b1=float(input("Ingrese la base menor del trapecio \n"
                    ">>>"))
            b2=float(input("Ingrese la base mayor del trapecio \n"
                    ">>>"))
            h=float(input("Ingrese la altura del trapecio \n"
                    ">>>"))
            area=(b1+b2)*h/2
        finally:
            print("Entiendo que no desea calcular ningún área \n"
                  "Hasta luego")
else:
    print("Entiendo que no desea calcular ningún área \n"
          "Hasta luego")
try:
    print(area)
except:
    pass
    
             
        
