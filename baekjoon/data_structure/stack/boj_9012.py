import sys
# sys.stdin = open("baekjoon/input.txt")
stack = []
t = (int)(sys.stdin.readline())
for _ in range(t):
    input_line = sys.stdin.readline().strip()

    for i in range(len(input_line)):
        if(stack):
            if(input_line[i]==')'):
                if(stack[-1]=='('):
                    stack.pop()
                else:
                    stack.append(input_line[i])
            else:
                  stack.append(input_line[i])
        else:
            stack.append(input_line[i])
        


    if(stack):
        print("NO")
    else:
        print("YES")
    stack = []