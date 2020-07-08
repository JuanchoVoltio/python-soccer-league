#Fechas
dates = {"06-02","07-02", "13-02", "14-02", "20-02", "21-02", "27-02", "28-02", "05-03","06-03", "12-03", "13-03", "19-03", "20-03", "26-03", "27-03"}
dias_ocupados_febrero = set()
dias_ocupados_marzo = set()
todos_los_dias = set()

for x in dates:
    if "02" in x:
        y = x.split("-")
        dias_ocupados_febrero.add(int(y[0]))
  
for x in dates:
    if "03" in x:
        y = x.split("-")
        dias_ocupados_marzo.add(int(y[0]))

for i in range(1,31,1):
    todos_los_dias.add(i)

print("")

print("=====FEBRERO=====")
print("Las días disponibles para el mes de Febrero son: ")
print(todos_los_dias.difference(dias_ocupados_febrero))

print("")

print("=====MARZO=====")
print("Las días disponibles para el mes de Marzo son: ")
print(todos_los_dias.difference(dias_ocupados_marzo))

print("")
