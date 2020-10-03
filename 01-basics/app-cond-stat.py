var = 42

if var >= 10:
    print("var is >= 10")
elif var >= 20:
    print("var is >= 20")

# str2 = var >= 10 ? "var is >= 10": "var < 10"
str = "var is >= 10" if var >= 10 else "var < 10"

for x in "my_string":
    print(x)

for i in range(2, 10):
    print(i)

print("/"*20)

# no float overload for y in range(2., 15., 1.5):
for y in range(2, 15, 2):
    print(y)

# list object and range object
print(type(range(0, 15)))
print(type([1, 2, 3, 4, 5]))
