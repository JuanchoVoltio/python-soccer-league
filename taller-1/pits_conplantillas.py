import random

tqmin=1 #tiempo_quitar_llanta_min
tqmax=1.3 #tiempo_quitar_llanta_max
tpmin=0.8 #tiempo_poner_llanta_min
tpmax=1.2 #tiempo_poner_llanta_max

temp="El tiempo del {} fue de {} segundos"

m1='mecanico 1 llanta 1'
m2='mecanico 2 llanta 1'
m3='mecanico 1 llanta 2'
m4='mecanico 2 llanta 2'
m5='mecanico 1 llanta 3'
m6='mecanico 2 llanta 3'
m7='mecanico 1 llanta 4'
m8='mecanico 2 llanta 4'

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

print(temp.format(m1,round(tm11,2)))
print(temp.format(m2,round(tm21,2)))
print(temp.format(m3,round(tm12,2)))
print(temp.format(m4,round(tm22,2)))
print(temp.format(m5,round(tm13,2)))
print(temp.format(m6,round(tm23,2)))
print(temp.format(m7,round(tm14,2)))
print(temp.format(m8,round(tm24,2)))

print("El tiempo de parada fue de ", tt, "segundos")
