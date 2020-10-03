var = 1
print(id(var))

var = var + 1
print(id(var))

++var
print(var)
print(id(var))
print("="*15)

list = [1, 2, 3]
print(list)
print(id(list))
list.append(4)
print(list)
print(id(list))
