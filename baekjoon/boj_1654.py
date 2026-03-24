import sys

input = sys.stdin.readline

k,n = map(int, input().split())

lenson=[]
for i in range(k):
    lenson.append(int(input()))

#정렬
lenson.sort()

left= 1
right= lenson[-1]

result =0

while(left <= right):
    mid = (left + right) // 2
    sum  = 0
    for x in lenson:
        sum += (x//mid)

    if sum >= n:
        result = mid
        left = mid+1
    else:
        right = mid-1

print(result)
