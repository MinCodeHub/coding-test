## BFS 

#### 📌 특징

- 큐(Queue, deque) 사용
- 가까운 노드부터 사용
- 최단 거리 문제에 강함
- 먼저 들어온 게 먼저 나감 (FIFO)

#### 그래프 초기화 (그래프 세팅)

```python

from collections import deque

n = int(input())
m = int(input())

graph = [[] for in range(n+1)]  #그래프 초기화

visited= [0] * (n+1)

```
#### 💻 BFS 코드

```python
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q: 
        cur = q.popleft()
        print(cur)

        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

```

## 🌳 DFS (Depth-First Search)

#### 📌 특징

- 스택 or 재귀
- 끝까지 깊게 들어감
- 백트래킹에 자주 사용

#### 💻 DFS 코드 (재귀)

```python
def dfs(cur):
    visited[cur] = True
    print(cur)

    for next in graph[cur]:
        if not visited[next]:
            dfs(next)
```

#### 💻 DFS 코드 (스택)

```python
def dfs(start):
    stack = [start]

    while stack:
        cur = stack.pop()

        if not visited[cur]:
            visited[cur] = True
            print(cur)

            for next in graph[cur]:
                if not visited[next]:
                    stack.append(next)

```

#### 핵심 흐름

1. 시작 노드 방문
2. 한 방향으로 계속 깊게 탐색
3. 더 이상 없으면 돌아옴(백트래킹)

