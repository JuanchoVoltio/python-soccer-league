print("WELCOME TO CAR SIMULATOR PROGRAM")

#PISTAS DE CARRERA
print("ESTAS SON LAS PISTAS DE CARRERA")

pistas=["Long_beach", "Interlagos", "Susuka", "Silverstone"]
pistas.append("Otra pista alternativa")
pistas.sort()
print(pistas)

#SELECCIONE LA PISTA A SIMULAR

seleccion_pistas=input("SELECCIONE LAA PISTA A CORRER:  ")
if seleccion_pistas in pistas:
    print("bienvenido a la pista: ", seleccion_pistas)
else:
    print("la pista no existe o ingresar otra pista alternativa")

#Bono por pista
#bonos
bono_chasis= 0.4
bono_motor= 0.6
bono_aerodinamica= 0.5
if seleccion_pistas=="Long_beach":
    print("cada piloto tiene bono Chasis y aerodinamica")
elif seleccion_pistas=="Interlagos":
    print("cada piloto tiene bono motor y chasis")
elif seleccion_pistas=="Susuka":
    print("cada piloto tiene bono aerodinamica y chasis")
elif seleccion_pistas=="Silverstone":
    print("cada piloto tiene bono motor y aerodinamica")
else:
    print("la pista no esta listada en la temporada")

#LISTA DE PILOTOS
print("ESTOS SON LOS PILOTOS")

pilotos=["piloto_1: C. Muños: bono chasis",\
         "Piloto_2: Kobayashi: bono motor",\
         "Piloto_3: P. Gchavez: bono aerodinamica",\
         "Piloto_4: P. Wherien: bono motor",\
         "Piloto_5: D.Riccardo: bono chasis"]

print(pilotos)



#tiempo de cada piloto
print("tiempos de cada piloto")

tiempo_piloto_1=float(input("ingrese el tiempo del piloto 1: "))
tiempo_piloto_2=float(input("ingrese el tiempo del piloto 2: "))
tiempo_piloto_3=float(input("ingrese el tiempo del piloto 3: "))
tiempo_piloto_4=float(input("ingrese el tiempo del piloto 4: "))
tiempo_piloto_5=float(input("ingrese el tiempo del piloto 5: "))


#orden de llegada


#tiempos de vuelta

tiempo_promedio = 67 or 70
# condiciones de tiempos por piloto

#posiciones y listado por orden de llegada

if (tiempo_piloto_1 > tiempo_piloto_2 and tiempo_piloto_1 >tiempo_piloto_3 and tiempo_piloto_1 >tiempo_piloto_4 and tiempo_piloto_1 >tiempo_piloto_5):
    print(" el ganador es el piloto_1", tiempo_piloto_1)
elif (tiempo_piloto_2 > tiempo_piloto_1 and tiempo_piloto_2 >tiempo_piloto_3 and tiempo_piloto_2 >tiempo_piloto_4 and tiempo_piloto_2 >tiempo_piloto_5):
    print("el ganador es el piloto_2")
elif (tiempo_piloto_3 > tiempo_piloto_1 and tiempo_piloto_3 >tiempo_piloto_2 and tiempo_piloto_3 >tiempo_piloto_4 and tiempo_piloto_3 >tiempo_piloto_5):
    print("el ganador es el piloto_3")
elif (tiempo_piloto_4 > tiempo_piloto_3 and tiempo_piloto_4 >tiempo_piloto_2 and tiempo_piloto_4 >tiempo_piloto_1 and tiempo_piloto_4 >tiempo_piloto_5):
    print("el ganador es el piloto_4")
elif (tiempo_piloto_5 > tiempo_piloto_4 and tiempo_piloto_5 >tiempo_piloto_3 and tiempo_piloto_5 >tiempo_piloto_2 and tiempo_piloto_5 >tiempo_piloto_1):
    print("el ganador es el piloto_5")
else:
    print("empate")
  #  print(tiempo_piloto_1)


