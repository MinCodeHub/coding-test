import sys

input = sys.stdin.readline

n = (int)(input().strip())

#입력받은 수를 정수로 바꾸고 set으로 저장
card = set(map(int,input().split()))

m = (int)(input())

find = map(int,input().split())

result=[]

for f in find:
    if f in card:
        result.append(1)
    else:
        result.append(0)

for i in range(m):
    print(result[i],end=" ")
