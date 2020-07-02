
import random

pilotos=["C. Muñoz", "Kobayashi", "G Chavez", "P. Wherlein", "D Ricciardo"]

bonos=["chasis", "motor", "aerodinamica", "motor", "chasis"]

pistas=("Long Beach", "Interlagos", "Suzuka", "Silverstone")

bonosdepista=("chasis-aerodinamica", "motor-chasis", "aerodinamica-chasis", "motor-aerodinamica")

for carrera in range (len(pistas)):
    tiempos=[]
    pilotoscarrera=[]
    pilotosinvertidos=[]
    for i in range (len(pilotos)):
        tiempogenerado=(70-67)*random.random()+67
        if bonosdepista[carrera].find(bonos[i]) >-1:
            if bonos[i]=="motor":
                tiempo=tiempogenerado-0.4
            elif bonos[i]=="chasis":
                tiempo=tiempogenerado-0.6
            elif bonos[i]=="aerodinamica":
                tiempo=tiempogenerado-0.5
        else:
            tiempo=tiempogenerado
        tiempos.append(round(tiempo,2))
    posiciones=tiempos.copy()
    posiciones.sort()
    posicionesinvertidas=tiempos.copy()
    posicionesinvertidas.sort(reverse=True)
    for i in range(len(tiempos)):
        a=tiempos.index(posiciones[i])
        b=tiempos.index(posicionesinvertidas[i])
        pilotoscarrera.append(pilotos[a])
        pilotosinvertidos.append(pilotos[b])

    #print(len(pilotos))
    #print(len(tiempos)) 
    print("\n Resultados de clasificación de la carrera de", pistas[carrera])
    for i in range (len(pilotos)):
        print(pilotoscarrera[i], posiciones[i], "segundos")

    print("\n Resultados de clasificación invertida de la carrera de", pistas[carrera])
    for i in range (len(pilotos)):
        print(pilotosinvertidos[i], posicionesinvertidas[i], "segundos")
