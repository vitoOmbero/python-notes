print("/"*20)

# lol
stlist = ["qwev", "kleb", "lew", "fvb", "eivf", "igsi", "ycgbayg"]

for s in stlist:
    if s.startswith("A"):
        print("Found!")
        break
else:
    print("Not found")

print("/"*20)

answer = 42
guess = 0

while answer != guess:
    guess = int(input("Guess the number: "))
else:
    pass
    # print("no")
print("Ok")
