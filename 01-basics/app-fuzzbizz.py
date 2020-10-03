def fizz_buzz(num: int) -> str:
    res: str
    flag = False
    if num % 3 == 0:
        res += "Fizz"
        flag = True
    if num % 5 == 0:
        res += "Buzz"
        flag = True
    if flag and num > 0:
        return res
    else:
        return str(num)


def go():
    for _ in range(0, 55):
        print(fizz_buzz(_))


go()
