import sys

input = sys.stdin.readline

n,m = map(int, input().split())

arr = list(map(int, input().split()))

#정렬 시간복잡도:O(N log N) 오래 걸림 
# arr.sort() 

left = 1
right = max(arr) #시간복잡도 :O(N) 가벼움, 배열 변경 없음
answer = 0
 
#총 시간 복잡도 O(log N) 이분탐색 + 전체 배열 순회 O(N)
while left <= right: 
    mid = (left+right)//2 
    total = 0 #벌목된 나무 총합
    for a in arr: 
        if a >= mid:
            total +=(a - mid)
    
    if total >= m:
        left = mid + 1
        answer = mid
    else:
        right = mid -1

print(answer)

