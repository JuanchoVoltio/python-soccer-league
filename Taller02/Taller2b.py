
mensaje=input("Ingrese el mensaje --->")

fin=int(len(mensaje))

if fin >3:
    print(mensaje[0:2], mensaje[fin-3:fin])
else:
    print("Cadena Vacia")
