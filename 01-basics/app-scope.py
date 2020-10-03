var = 0


def foo():
    var = 2
    print(var)


def fua():
    var = 1


def fup():
    global var
    var = 42


print(foo())
print()
fua()
print(var)
fup()
print(var)
