def recursive_addition(num):
  if(num > 0):
    print("Adding: " + str(num) + " + sum(" + str(num-1) + ")")
    result = num + recursive_addition(num -1)
    return result

  return 0


print(recursive_addition(10))
