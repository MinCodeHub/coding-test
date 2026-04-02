n = int(input())

arr = set(map(int, input().split()))

m = int(input())
target = list(map(int, input().split()))

for t in target:
    if t in arr:
        print(1)
    else:
        print(0)