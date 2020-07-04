pregunta = input('¿Quieres hacer una pregunta? ')

while pregunta == 'si':
    pregunta = input('¿Quieres hacer otra pregunta? ')
    if  pregunta == "no":
        break
    respuesta = input("Esta es la respuesta: ")

    if respuesta == "porque si":
        break