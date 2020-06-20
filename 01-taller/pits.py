import random 
#Programa de simulación de pits para indicar
#Definir las variables
tires = 4

#Simular tiempos para cada mecanico
time_crew_member_1 = round(random.uniform(0.1,10),2)
time_crew_member_2 = round(random.uniform(0.1,10),2)
time_crew_member_3 = round(random.uniform(0.1,10),2)
time_crew_member_4 = round(random.uniform(0.1,10),2)

#Mostrar el resultado del trabajo de pits
#1.Tiempos de cada mecanico
#2.Mostrar tiempo total de la parada de pits
print(time_crew_member_1)
print(time_crew_member_2)
print(time_crew_member_3)
print(time_crew_member_4)

total = max([time_crew_member_1, time_crew_member_2, time_crew_member_3, time_crew_member_4])
print("El tiempo total en pits fue: ")
print(str(total) + 's')