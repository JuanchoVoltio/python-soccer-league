import random

print("Bienvenido al simulador de dados de Python Soccer Leage")

repeticiones=input("¿Cuántos dados desea lanzar?")

n=int(repeticiones)+1

for dado in range (1,n):
    print("Dado ", dado, " = ", random.randint(1,6))
