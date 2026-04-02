from collections import deque

n,m,v = map(int, input().split())


graph =[[] for _ in range(n+1)] #그래프 초기화
visited = [False] * (n+1) #방문여부 초기화
result = [] #결과값 초기화


def dfs(cur):
     result.append(cur)
     visited[cur] = True
    
     for next in graph[cur] : 
        if not visited[next]:
            dfs(next)





def bfs(cur):
    q = deque()
    visited[cur] = True
    q.append(cur) 
    result.append(cur) # 시작 노드 추가

    while q:
        cur = q.popleft()

        for i in graph[cur]:
            if not visited[i] :
                visited[i] = True
                q.append(i)
                result.append(i)
            
        

for i in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)   
    graph[n2].append(n1)

for i in range(1, n+1):
    graph[i].sort()

dfs(v)
print(*result)

visited = [False] * (n+1) #방문여부 초기화
result = [] #결과값 초기화

bfs(v)
print(*result);





