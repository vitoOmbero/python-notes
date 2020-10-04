nums = [1, 1, 3, 4, 4, 7, 3, 4]

unq = set(nums)

print(unq)

myset = {1, 3, 3, 4, 9}
myset.add(3)

print(myset)

myset.remove(3)

print(myset)


nset = unq | myset
print("nset", nset)
mset = unq & myset
print("mset", mset)

print(" - :", unq - myset)
print(" ^ :", unq ^ myset)

if 1 in unq:
    print("1 in unq")
