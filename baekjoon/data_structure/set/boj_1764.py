import sys

#sys.stdin = open("baekjoon/input.txt")
n,m = map(int,sys.stdin.readline().split()) #리스트 반환


heard=set()
seen = set()

for _ in range(n):
   heard.add(sys.stdin.readline().strip())

for _ in range(m):
    seen.add(sys.stdin.readline().strip())

result = sorted(heard & seen)

print(len(result))

for i in range(len(result)):
    print(result[i])