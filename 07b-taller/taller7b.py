import random

class F1Driver:
    def __init__(self, name, bonus=0):
        self.name = name
        self.bonus = bonus

    def tiempos(self):
        return str(round(random.uniform(67,70),2))



class pistas:
    def __init__(self, muñoz, Kobayachi, chavez, wherlein, ricciardo):
        self.muñoz = muñoz
        self.kobayachi = Kobayachi
        self.chavez = chavez 
        self.wherlein = wherlein
        self.ricciardo = ricciardo

    def longbeach(self):
        long_beach = [str(self.muñoz - 0.5)+"s: Muñoz,", str(self.kobayachi)+"s: kobayachi,", str(self.chavez - 0.5)+"s: Chavez,", str(self.wherlein)+"s: Wherlein,", str(self.ricciardo - 0.6)+"s: Ricciardo"]
        print("")
        print("=====LONGBEACH=====")
        print("")
        print("La clasificacion para la pista de Longbeach fue: ")
        print(sorted(long_beach))
        print("")
        print("Para la carrera saldran de la siguiente manera: ")
        print(sorted(long_beach, reverse=True))
        print("")

    def interlagos(self):
        interlago = [str(self.muñoz)+"s: Muñoz,", str(self.kobayachi - 0.4)+"s: kobayachi,", str(self.chavez)+"s: Chavez,", str(self.wherlein - 0.4)+"s: Wherlein,", str(self.ricciardo - 0.6)+"s: Ricciardo"]
        print("")
        print("=====INTERLAGOS=====")
        print("")
        print("La clasificacion para la pista de Interlagos fue: ")
        print(sorted(interlago))
        print("")
        print("Para la carrera saldran de la siguiente manera: ")
        print(sorted(interlago, reverse=True))
        print("")

    def suzuka(self):
        suzukas = [str(self.muñoz - 0.5)+"s: Muñoz,", str(self.kobayachi)+"s: kobayachi,", str(self.chavez - 0.5)+"s: Chavez,", str(self.wherlein)+"s: Wherlein,", str(self.ricciardo - 0.6)+"s: Ricciardo"]
        print("")
        print("=====SUZUKA=====")
        print("")
        print("La clasificacion para la pista de Suzuka fue: ")
        print(sorted(suzukas))
        print("")
        print("Para la carrera saldran de la siguiente manera: ")
        print(sorted(suzukas, reverse=True))
        print("")

    def silverstone(self):
        silverston = [str(self.muñoz - 0.5)+"s: Muñoz,", str(self.kobayachi - 0.4)+"s: kobayachi,", str(self.chavez - 0.5)+"s: Chavez,", str(self.wherlein - 0.4)+"s: Wherlein,", str(self.ricciardo)+"s: Ricciardo"]
        print("")
        print("=====Silverstone=====")
        print("")
        print("La clasificacion para la pista de Silverstone fue: ")
        print(sorted(silverston))
        print("")
        print("Para la carrera saldran de la siguiente manera: ")
        print(sorted(silverston, reverse=True))
        print("")

#print(isinstance(muñoz,float))

#================TIEMPOS============================
muñoz = float(F1Driver('Muñoz').tiempos())
Kobayachi = float(F1Driver('Kobayachi').tiempos())
chavez = float(F1Driver('chavez').tiempos())
wherlein = float(F1Driver('wherlein').tiempos())
ricciardo = float(F1Driver('ricciardo').tiempos())


#==================CARRERAS=======================
pistas(muñoz, Kobayachi, chavez, wherlein, ricciardo).longbeach()
pistas(muñoz, Kobayachi, chavez, wherlein, ricciardo).interlagos()
pistas(muñoz, Kobayachi, chavez, wherlein, ricciardo).suzuka()
pistas(muñoz, Kobayachi, chavez, wherlein, ricciardo).silverstone()



