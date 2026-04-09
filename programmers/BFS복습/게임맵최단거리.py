from collections import deque

def solution(maps):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    
    n = len(maps)
    m = len(maps[0])

    
    q = deque()
    q.append((0,0,1))
    visited = set()
    answer = -1
    while (q):
        x,y,cnt = q.popleft();
        if x == n-1 and y == m-1:
            answer = cnt
            break

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx >= n or nx < 0 or ny >= m or ny < 0 :
                continue
            if (nx,ny) not in visited: #문법 주의 not in !!!!!
                if maps[nx][ny] == 1:
                       q.append((nx,ny,cnt+1))
                       visited.add((nx,ny))

    return answer