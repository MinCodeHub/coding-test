import sys
from collections import deque

# sys.stdin = open("baekjoon/input.txt")
queue = deque()

n = (int)(sys.stdin.readline())


for _ in range(n):
    input_line = sys.stdin.readline().split()
    command  =input_line[0]

    if(command == "push"):
        num = input_line[1]
        queue.append(num)
    elif(command=="pop"):
        if(queue):
             print(queue.popleft())
        else:
            print(-1)
        
    elif(command=="size"):
        print(len(queue))
    elif(command=="empty"):
        if(queue):
            print(0)
        else:
            print(1)
    elif(command=="front"):
        if(queue):
            print(queue[0])
        else:
            print(-1)
    elif(command=="back"):
        if(queue):
            print(queue[-1])
        else:
            print(-1)


