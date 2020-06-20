
tqmin=1 #tiempo_quitar_llanta_min
tqmax=1.3 #tiempo_quitar_llanta_max
tpmin=0.8 #tiempo_poner_llanta_min
tpmax=1.2 #tiempo_poner_llanta_max

import random

tm11= (tqmax-tqmin)*random.random()+tqmin #tiempo mecanico 1 llanta 1
tm21= (tpmax-tpmin)*random.random()+tpmin #tiempo mecanico 2 llanta 1
t1=tm11+tm21 #tiempo llanta 1

tm12= (tqmax-tqmin)*random.random()+tqmin #tiempo mecanico 1 llanta 2
tm22= (tpmax-tpmin)*random.random()+tpmin #tiempo mecanico 2 llanta 2
t2=tm12+tm22 #tiempo llanta 2

tm13= (tqmax-tqmin)*random.random()+tqmin #tiempo mecanico 1 llanta 3
tm23= (tpmax-tpmin)*random.random()+tpmin #tiempo mecanico 2 llanta 3
t3=tm13+tm23 #tiempo llanta 3

tm14= (tqmax-tqmin)*random.random()+tqmin #tiempo mecanico 1 llanta 4
tm24= (tpmax-tpmin)*random.random()+tpmin #tiempo mecanico 2 llanta 4
t4=tm14+tm24 #tiempo llanta 1

tt=round(max(t1, t2 ,t3, t4),2) #tiempo total

print("El tiempo de parada fue de ", tt, "segundos")
