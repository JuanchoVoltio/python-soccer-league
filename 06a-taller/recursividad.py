def recursive_adition(num):
    if num > 0:
        print("Adding: "+ str(num) + " + sum(" + str(num-1)+")")
        result = num + recursive_adition(num - 1)
        return result
    return 0

#print(recursive_adition(10))


def cuenta_digitos(n):
    if n<10:
        return 1
    else:
        return 1 + cuenta_digitos(n/10)


print(cuenta_digitos(10))
    