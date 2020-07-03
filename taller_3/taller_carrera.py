import random
#se daran los siguientes bonos por tipo de xigencia de la carrera
bono_motor = 0.4
bono_chasis = 0.6
bono_aerodinamica = 0.5

#los pilotos tienen los siguientes bonos:
#muñoz = clasificacion - bono_chasis
#kobayachi = clasificacion - bono_motor
#chavez = clasificacion - bono_aerodinamica
#wherlein = clasificacion - bono_motor
#ricciardo = clasificacion - bono_chasis

#pista de Longbeach (bono chasis y aerodinamica)

#simulacion tiempos aleatorios de clasificacion

muñoz = round(random.uniform(67,70),2) - bono_aerodinamica # se establecen 2 cifras decimas
kobayachi = round(random.uniform(67,70),2)
chavez = round(random.uniform(67,70),2) - bono_aerodinamica
ricciardo = round(random.uniform(67,70),2) - bono_chasis
wherlein = round(random.uniform(67,70),2)



long_beach = [str(muñoz)+" segungos > piloto Muñoz", str(kobayachi)+" segungos > piloto kobayachi", str(chavez)+" segungos > piloto Chavez", str(wherlein)+" segungos > piloto Wherlein", str(ricciardo)+" segungos > piloto Ricciardo"]
print("")
print("**********TIEMPOS DE CLASIFICACION PARA LA PISTA DE LONGBEACH**********")
print("")
print("")
print("Los tiempos de  clasificacion para la pista de Longbeach quedaron de la siguiente manera: ")
print("")
print("")
print(long_beach[0])
print(long_beach[1])
print(long_beach[2])
print(long_beach[3])
print(long_beach[4])
primera_carrera=sorted(long_beach)
segunda_carrera=sorted(long_beach, reverse=True)
print("")
print("***LOS PILOTOS SALDRAN EN EL SIGUIENTE ORDEN PARA LA PRIMERA CARRERA: ***")
print("")
print("")
print(primera_carrera[0])
print(primera_carrera[1])
print(primera_carrera[2])
print(primera_carrera[3])
print(primera_carrera[4])
print("")
print("***LOS PILOTOS SALDRAN EN EL SIGUIENTE ORDEN PARA LA SEGUNDA CARRERA (PARRILLA INVERTIDA): ***")
print("")
print("")
print(segunda_carrera[0])
print(segunda_carrera[1])
print(segunda_carrera[2])
print(segunda_carrera[3])
print(segunda_carrera[4])
print("")

