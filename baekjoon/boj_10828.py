import sys

# 입력의 개수 N을 받음
n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    # sys.stdin.readline()으로 입력 받고, 공백을 기준으로 명령어를 구분
    input_line = sys.stdin.readline().split()
    command = input_line[0]

    if command == "push":
        # push 명령어의 경우, 두 번째 요소(정수)를 스택에 추가
        stack.append(int(input_line[1]))
    elif command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        # 스택이 비어있는지 확인
        print(0 if stack else 1)
    elif command == "top":
        if stack:
            print(stack[-1])  # 스택의 마지막 요소(가장 위에 있는 정수)를 출력
        else:
            print(-1)