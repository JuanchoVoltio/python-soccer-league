import operator
bono_motor = 0.4
bono_chasis = 0.6
bono_aerodinamica = 0.5
class F1Driver:

 def __init__(self,name,bonus,tiempos):
  self.name = name #debe ser inicializado
  self.bonus = bonus #debe ser inicializado
  self.tiempos=tiempos

 
 

 def clasificacion(self):
     import random
     if self.bonus=="aerodinamica":
       self.tiempos=round(random.uniform(67,70),2) - bono_motor
     elif self.bonus=="chasis":
       self.tiempos=round(random.uniform(67,70),2) - bono_chasis
     elif self.bonus=="aerodinamica":
       self.tiempos=round(random.uniform(67,70),2) - bono_aerodinamica
     
     else:self.tiempos=round(random.uniform(67,70),2)

     print("tiempo de clasificacion del piloto",self.name,"es", self.tiempos,"segundos.")
 
     
  

#---------------- FIN DE LA DEFINICION DE LA CLASE F1Driver ---------------



print("***Los tiempo de clasificacion son los siguientes: ***")
print("")
print("")
driver1 = F1Driver("Muñoz", "aerodinamica","")
driver2 = F1Driver("kobayachi", "","")
driver3 = F1Driver("Chavez", "aerodinamica","")
driver4 = F1Driver("Ricciardo", "chasis","")
driver5 = F1Driver("Wherlein", "","")
driver1.clasificacion()
driver2.clasificacion()
driver3.clasificacion()
driver4.clasificacion()
driver5.clasificacion()


long_beach = {driver1.tiempos:driver1.name,driver2.tiempos:driver2.name,driver3.tiempos:driver3.name,driver4.tiempos:driver4.name,driver5.tiempos:driver5.name}
print("")

