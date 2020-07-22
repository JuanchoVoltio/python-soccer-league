def recursive_adition(num):
    if num > 0:
        print("Adding: "+ str(num) + " + sum(" + str(num-1)+")")
        result = num + recursive_adition(num - 1)
        return result
    return 0

#print(recursive_adition(10))


def cuenta_digitos(n):
    #result = cuenta_digitos(n/10) 
    result = n/10
    if result > 0:
        cuenta_digitos(n/10)
        print (result) 




print(cuenta_digitos(100))
    