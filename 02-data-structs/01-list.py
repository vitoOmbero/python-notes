def l():
    print("*"*50)


letters = ["q", "w", "e", "r"]
print(letters)
l()

matrix = [[1, 0], [0, 1]]
print(matrix)
l()

z = [2] * 13
print(z)
l()

combo = z + letters
print(combo)
l()

nums = list(range(20))
print(nums)
l()

char_str = list("alialsba")
print(char_str)
l()
l()

print(len(z))


print(letters[-1])
letters[2] = 'Q'
print(letters[2:])

full_copy = letters[:]
part_copy = letters[::2]
print(full_copy)
print(part_copy)

reversed_copy = letters[::-1]
print(reversed_copy)

l()
l()
# list unpacking
print("list unpacking")
my_nums = [2, 5, 76, 23, 54, 67, 89]
fir, sec, *rest_nums, last = my_nums

print(fir)
fir = 42
print(my_nums[0])
print(rest_nums)

l()
l()
# loop
print("loop")

for letter in enumerate(letters):
    print(letter)
l()
# enumerate returns std::pair cosplay
for letter in enumerate(letters):
    print(letter[0], letter[1])
l()
# tuple can be unpacked
for ind, val in enumerate(letters):
    print(ind, val)
l()

l()
l()
# modify
print("modify")

letters.append("n")
letters.insert(1, "X")

print(letters)

cp: list = ([0]*7 + letters)[::2]
print(cp)
cp.pop(0)
print(cp)
cp.remove("Q")
print(cp)
del cp[0:3]
print(cp)
cp.clear()
print(cp)


l()
l()
# special
print("special")

slist = ["q", "w", "e", "r"]
# error: print(slist.index("Q"))
if "Q" in slist:
    print(slist.index("Q"))

if slist.count("Q") == 0:
    print("no such element")

l()
l()
# sort
print("sort")

my_nums.sort(reverse=True)
print(my_nums)
smy_list = sorted(my_nums)
print(smy_list)
l()

tuplist = [
    ("Abe", 645),
    ("Qpy", 978),
    ("Zwe", 111),
]

tuplist.sort()
print(tuplist)


def get_second(item):
    return item[1]


tuplist.sort(key=get_second)
print(tuplist)
