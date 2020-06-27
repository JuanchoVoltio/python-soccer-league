import random

bono_motor = 0.4
bono_chasis = 0.6
bono_aerodinamica = 0.5

#muñoz = clasificacion - bono_aerodinamica
#kobayachi = clasificacion - bono_motor
#chavez = clasificacion - bono_aerodinamica
#wherlein = clasificacion - bono_motor
#ricciardo = clasificacion - bono_chasis

#==============Longbeach (bono chasis y aerodinamica)=========================

muñoz = round(random.uniform(67,70),2) - bono_aerodinamica
kobayachi = round(random.uniform(67,70),2)
chavez = round(random.uniform(67,70),2) - bono_aerodinamica
wherlein = round(random.uniform(67,70),2)
ricciardo = round(random.uniform(67,70),2) - bono_chasis


long_beach = [str(muñoz)+"s: Muñoz,", str(kobayachi)+"s: kobayachi,", str(chavez)+"s: Chavez,", str(wherlein)+"s: Wherlein,", str(ricciardo)+"s: Ricciardo"]
print("")
print("=====LONGBEACH=====")
print("")
print("La clasificacion para la pista de Longbeach fue: ")
print(sorted(long_beach))
print("")
print("Para la carrera saldran de la siguiente manera: ")
print(sorted(long_beach, reverse=True))
print("")

#==============================================================================


#==============Interlagos (bono motor y chasis)================================

muñoz = round(random.uniform(67,70),2)
kobayachi = round(random.uniform(67,70),2) - bono_motor
chavez = round(random.uniform(67,70),2) 
wherlein = round(random.uniform(67,70),2) - bono_motor
ricciardo = round(random.uniform(67,70),2) - bono_chasis

interlagos = [str(muñoz)+"s: Muñoz,", str(kobayachi)+"s: kobayachi,", str(chavez)+"s: Chavez,", str(wherlein)+"s: Wherlein,", str(ricciardo)+"s: Ricciardo"]
print("")
print("=====INTERLAGOS=====")
print("")
print("La clasificacion para la pista de Interlagos fue: ")
print(sorted(interlagos))
print("")
print("Para la carrera saldran de la siguiente manera: ")
print(sorted(interlagos, reverse=True))
print("")

#==============================================================================


#==============Suzuka (bono aerodinamica y chasis)================================

muñoz = round(random.uniform(67,70),2) - bono_aerodinamica
kobayachi = round(random.uniform(67,70),2)
chavez = round(random.uniform(67,70),2) - bono_aerodinamica
wherlein = round(random.uniform(67,70),2)
ricciardo = round(random.uniform(67,70),2) - bono_chasis

suzuka = [str(muñoz)+"s: Muñoz,", str(kobayachi)+"s: kobayachi,", str(chavez)+"s: Chavez,", str(wherlein)+"s: Wherlein,", str(ricciardo)+"s: Ricciardo"]
print("")
print("=====SUZUKA=====")
print("")
print("La clasificacion para la pista de Suzuka fue: ")
print(sorted(suzuka))
print("")
print("Para la carrera saldran de la siguiente manera: ")
print(sorted(suzuka, reverse=True))
print("")

#============================================================================================


#==============Silverstone (bono motor y aerodinamica)================================
muñoz = round(random.uniform(67,70),2) - bono_aerodinamica
kobayachi = round(random.uniform(67,70),2) - bono_motor
chavez = round(random.uniform(67,70),2) - bono_aerodinamica
wherlein = round(random.uniform(67,70),2) - bono_motor
ricciardo = round(random.uniform(67,70),2) 

silverstone = [str(muñoz)+"s: Muñoz,", str(kobayachi)+"s: kobayachi,", str(chavez)+"s: Chavez,", str(wherlein)+"s: Wherlein,", str(ricciardo)+"s: Ricciardo"]
print("")
print("=====Silverstone=====")
print("")
print("La clasificacion para la pista de Silverstone fue: ")
print(sorted(silverstone))
print("")
print("Para la carrera saldran de la siguiente manera: ")
print(sorted(silverstone, reverse=True))
print("")