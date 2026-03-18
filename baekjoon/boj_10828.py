n = int(input())
stack = []
result = []

for i in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        stack.append(cmd[1])

    elif cmd[0] == "pop":
        if len(stack) == 0:
            result.append("-1")
        else:
            result.append(stack.pop())

    elif cmd[0] == "size":
        result.append(str(len(stack)))

    elif cmd[0] == "empty":
        if len(stack) == 0:
            result.append("1")
        else:
            result.append("0")

    elif cmd[0] == "top":
        if len(stack) == 0:
            result.append("-1")
        else:
            result.append(stack[-1])

#한 번에 출력
print("\n".join(result))