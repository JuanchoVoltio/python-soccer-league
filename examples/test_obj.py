class F1Driver:

 def __init__(self,name,bonus):
  self.name = name #debe ser inicializado
  self.bonus = bonus #debe ser inicializado

 def radio_chat(message):
  print("Leave me alone, I know what I'm doing")

 def get_about(self):
  answer = ""
  #Iterar la coleccion de bonus y concatenar valores.
  print("I’m " + self.name + ", " + self.bonus + " specialist.")

#---------------- FIN DE LA DEFINICION DE LA CLASE F1Driver ---------------


driver1 = F1Driver("Kimi", "chassis")
driver2 = F1Driver("Schucmacher", "aero")
driver1.team = "McLaren"
print(driver1.team)
driver1.team = "Ferrari"
print(driver1.team)
driver1.get_about()
driver2.get_about()
