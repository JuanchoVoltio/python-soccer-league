#definimos el nombre del programa  y la bienvenida
print(" project pits for furmula 1")
print("welcome to the pit simulator with 8 crew members")

print("crew members time")
#definimos la variables
time_crew_team_tire1=float(5.4)
time_crew_team_tire2=float(0.5)
time_crew_team_tire3=float(2.1)
time_crew_team_tire4=float(1)

#mostramos el tiempo tomado por cada equipo
print("member 1 time: ", time_crew_team_tire1, "seconds")
print("member 2 time: ", time_crew_team_tire2, "seconds")
print("member 3 time: ", time_crew_team_tire3, "seconds")
print("member 4 time: ", time_crew_team_tire4, "seconds")


#calculamos el tiempo total del equipo para cambiar las 4 llantas
Total_Tire_Replacement_Time= time_crew_team_tire1+time_crew_team_tire2+time_crew_team_tire3+time_crew_team_tire4
print("TOTAL CREW TEAM TIRE TIME IS: ", Total_Tire_Replacement_Time, "seconds")
