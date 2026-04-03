from collections import deque
n,m = map(int, input().split())

#입력
#input().strip() -> 문자열 "101111"
#map(int, ...) → 각각 '1','0' → 숫자로 변환
#list(...) → [1,0,1,1,1,1]


graph =[list(map(int, input().strip())) for _ in range(n)]
#visited = [[0]*(m) for _ in range(n)]

def bfs(x,y):

    dx=[0,1,0,-1]
    dy=[1,0,-1,0]

    q = deque()
    q.append((x,y))
    
    while(q):
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx>=n or ny<0 or ny >=m:
                continue
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))

    return graph[n-1][m-1]


print(bfs(0,0))

