#definimos el nombre del programa  y la bienvenida
print("proyecto pit")
print("bienvenido al simulador de parada de pits")

#definimos la variables
print("crew members time")

time_crew_member_1=float(5.4)
time_crew_member_2=float(3.5)
time_crew_member_3=float(2.1)
time_crew_member_4=float(1)
fuel_supply_full=float(100)

#mostramos el tiempo tomado por cada miembro
print("member 1 time: ", time_crew_member_1, "seconds")
print("member 2 time: ", time_crew_member_2, "seconds")
print("member 3 time: ", time_crew_member_3, "seconds")
print("member 4 time: ", time_crew_member_4, "seconds")


#repostaje de combustible
print("fuel tank galons is: ", fuel_supply_full,"galons")

#calculamos el tiempo total del equipo para cambiar las 4 llantas
Total_Tire_Replacement_Time= time_crew_member_1+time_crew_member_2+time_crew_member_3+time_crew_member_4
print("TOTAL CREW TIRE TIME IS: ", Total_Tire_Replacement_Time, "seconds")





