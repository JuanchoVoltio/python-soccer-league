import math

radio = float(input("Ingrese el radio del circulo en centimetro. Para calcular su area: "))

area = round((radio**2) * round(math.pi,4),2)


print("El area de un circulo con radio {0} cm es: {1} cm o {2} m".format(radio, area, area/100))