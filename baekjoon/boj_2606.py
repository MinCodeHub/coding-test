from collections import deque

def bfs():
    q = deque()
    count = 0
    q.append(1)
    visited[1] = 1

    while q:
        cur = q.popleft()

        for i in net[cur]:
            if visited[i] == False:
                visited[i]= True
                q.append(i)
                count+=1
    print(count)

n= int(input()) #컴퓨터 개수
m = int(input()) #연결선 개수

net = [[] for _ in range(n+1)] #방문 체크

for _ in range(m): #연결 관계 그래프
    a,b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

visited = [0] * (n+1)

bfs()



