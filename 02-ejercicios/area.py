import math

radio = float(input("Ingrese el radio del circulo en centimetro. Para calcular su area: "))

area = round((radio**2) * round(math.pi,4),2)

print("El area de un circulo con radio "+ str(radio) + " cm es: " + str(area) + " cm o " + str(area/100) + " m")

