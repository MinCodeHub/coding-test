import sys

input = sys.stdin.readline

n,m = map(int, input().split())

arr = list(map(int, input().split()))

#정렬
arr.sort()

left = 1
right = arr[-1]
answer = 0

while(left <= right):
    mid = (left+right)//2
    total = 0
    for a in arr: #해당포문때문에 시간초과
        if a > mid:
            total +=(a - mid)
    
    if total >= m:
        left = mid + 1
        answer = mid
    else:
        right = mid -1

print(answer)

