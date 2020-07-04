#Figura 1
"""
h=5
b=6
for i in range(0,h,1):
    print("*"*b)
"""
#==================================




#Figura 2
"""
h = 5
for i in range(0,1,1):
    for j in range(0,h,1):
        print("*" + "*"*j)
"""
#=================================



#Figura 3
"""

b=7
espacios=0

for j in range(b,0,-2):
    print(" "*espacios+ "*"*j + " "*espacios)
    espacios += 1
""" 
#======================================



#Figura 4

b=6
espacios=0

for j in range(b,0,-2):
    print(" "*espacios+ "*"*j + " "*espacios)
    espacios += 1
    if j == 2:
        for i in range(0,b+1,2): 
            print(" "*espacios + "*"*i + " "*espacios) 
            espacios -= 1
    
