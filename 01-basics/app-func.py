def do_nothing():
    pass


print(do_nothing())
print(type(do_nothing))
print(type(do_nothing()))

print(20*"*")


def inc(arg, by):
    return arg + by


print(inc(6, 2))
print(inc(6, 2.4))
print(inc(True, False))
print(inc("str0", "1"))

# tuples are built-in
print(20*"*")


def inc_tup(arg, by=1):
    res = arg+by
    return (type(res), res)


print(inc_tup(6, 2))
print(type(inc_tup(6, 2)))
print(inc_tup(6, by=2.4))
print(inc_tup(True, False))
print(inc_tup("str0", "1"))

# python has strong typing
print(20*"*")
try:
    print(inc_tup("str0"))
except:
    print("It shall not pass!")

# ... but python still has dynamic typing!
print(20*"*")


def inc_tup2(arg: int, by: int = 1) -> tuple:
    res = arg+by
    return (type(res), res)


print(inc_tup2("str0", "1"))

# varargs
print(20*"*")


def mul(*list: int) -> int:
    res = 1
    for num in list:
        res *= num
    return res


print(mul(2, 4, 6, 23, 42.))


# python magic
print(20*"*")


def show_user(**user):
    print(user)


show_user(id=1, name="admin", flags=bin(0b001001110110))


def show_user_id(**user):
    print(user["id"])


def show_user_pass(**user):
    print(user["pass"])


show_user_id(id=1, name="admin", flags=bin(0b001001110110))
show_user_pass(id=1, name="admin", flags=bin(0b001001110110))
