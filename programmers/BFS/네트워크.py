from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(len(computers))]
    #1. 본인이 아닌데 1이면 둘이 연결되어 있다는 것.
    #2.  방문 배열 만들기
    # commputers를 순회하면서 방문을 안했다면 bfs호출
    # 큐가 끝나면 answer에 1 더해줌
    # computers 순회 계속..
    
    for i in range(len(computers)):
        if visited[i] == False :
            answer+=1
            bfs(i,computers, visited)
           

    return answer

def bfs(start,computers,visited):
    
    q = deque()
    q.append(start)
    visited[start] = True
    
    while(q):
        node = q.popleft()
        for i in range(len(computers)):
            if not visited[i] and computers[node][i] == 1:
                visited[i] = True
                q.append(i)
    
    
    
