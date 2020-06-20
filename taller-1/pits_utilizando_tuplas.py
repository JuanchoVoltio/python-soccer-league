number_tires = ("primera llanta","segunda llanta","tercera llanta","cuarta llanta")
tiempo_change = ("4","3.5","3","4.9")
#tiempos de cambio de cada llanta


#Para mostrar el tiempo de cada cambio de llanta se utiliza la fincion print

#2.Mostrar tiempo total de la parada de pits
print("El siguiente programa muesta la duracion de un carro en pits")
print("El tiempo en cambiar la", number_tires[0],"fue" ,tiempo_change[0], "segundos")
print("El tiempo en cambiar la", number_tires[1],"fue" ,tiempo_change[1], "segundos")
print("El tiempo en cambiar la", number_tires[2],"fue" ,tiempo_change[2], "segundos")
print("El tiempo en cambiar la", number_tires[3],"fue" ,tiempo_change[3], "segundos")

#realiza la comparacion con la funcion if entre los 4 tiempos y verifica cual es el tiempo mayor

tiempo_pits = tiempo_change[3]
print("El tiempo en pits fue: ", tiempo_pits, "segundos")

