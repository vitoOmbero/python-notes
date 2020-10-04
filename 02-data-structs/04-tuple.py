point = (1, 2)

p2 = 4, 3
p3 = ()

print(type(point))
print(type(p2))
print(type(p3))

p3 = p2 + point
print(p3)
print(type(p3))

p4 = tuple([1, 2])
p5 = tuple("string")
p6 = tuple("qwe"*3)
print(type(p4))
print(type(p5))
print(type(p6))
print(p6)

coord = 23, 56, 73
x, y, z = coord

if 10 in coord:
    print("exists")

# are immutable coord[0] = 10
