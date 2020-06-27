cadena_caracteres = str(input("Ingrese una cadena de caracteres: "))


longitud_cadena = len(cadena_caracteres)



if longitud_cadena > 3:
    primeras = cadena_caracteres[0] + cadena_caracteres[1]
    ultimas = cadena_caracteres[longitud_cadena-3] + cadena_caracteres[longitud_cadena-2] + cadena_caracteres[longitud_cadena-1] 
    print(primeras + ultimas)
else:
    print(" ")


