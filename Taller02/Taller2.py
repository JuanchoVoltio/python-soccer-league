
mensaje="programoenpythonymediviertoalaprenderperosinpausaysinprisa"

inicio=int(mensaje.find("divierto"))

fin=int(len("divierto"))+inicio

if inicio >-1:
    mensaje1=mensaje[inicio:fin]
    print(mensaje1)
else:
    print("El mensaje no contiene el texto divertido")
