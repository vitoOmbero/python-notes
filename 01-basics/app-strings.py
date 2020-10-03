str = "some string"
print(len(str))

print(str[0])
print(str[-1])
print(str[-1:3])
print(str[-1:-3])
print(str[-3:-1])
print(str[0:3])
print(str[:3])
print(str[0:])
print(str[:])

s2 = str[:4]

print(id(str))
print(id(s2))
print(id(str[:4]))
