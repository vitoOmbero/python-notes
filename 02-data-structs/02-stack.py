stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.append(6)
print(stack)

last = stack.pop()
print("last", last)
print(stack)

if not stack:
    print("stack is empty")
else:
    print("stack is not empty")

while True:
    if stack:
        print("last:", stack[-1])
        print("pop(): ", stack.pop())
        print("stack: ", stack)
    else:
        print("stack is empty")
        break
