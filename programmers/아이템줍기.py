from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    #좌표 2배
    #rectangle 안에 있는 모든 좌표를 하나씩 꺼내서 2배 해서 다시 넣는다.
    #[변환값 for 꺼낼값 in 리스트]
    rectangle = [[x*2, y*2, x2*2, y2*2] for x,y,x2,y2 in rectangle]
    
    characterX *=2
    characterY *=2
    itemX *=2
    itemY *=2
    
    #전체 0으로 초기화
    graph = [[0] * 102 for _ in range(102) ]
    visited= [[False] * 102 for _ in range(102)]
    #전체 1로 초기화
    for x1, y1, x2, y2 in rectangle:
        for j in range(x1,x2+1):
            for k in range(y1, y2+1):
                graph[j][k] = 1
                
    # 사각형 내부만 다시 0으로 
    for x1, y1, x2, y2 in rectangle:
         for j in range(x1+1,x2):
            for k in range(y1+1, y2):
                graph[j][k] = 0
    
    dx= [0,1,0,-1]
    dy = [1,0,-1,0]
    
    q = deque()
    q.append((characterX,characterY,1))
    visited[characterX][characterY] = True
    while q:
        x,y,cnt = q.popleft()
        
        if x == itemX and y == itemY:
            answer = cnt
            break
        
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0 <= nx < 102 and 0 <= ny < 102:  
                if graph[nx][ny] == 1:
                    if not visited[nx][ny]:
                        q.append((nx,ny,cnt+1))
                        visited[nx][ny] = True
        
    return answer//2


    
    