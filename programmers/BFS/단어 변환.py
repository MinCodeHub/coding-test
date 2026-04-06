from collections import deque

def solution(begin, target, words):

    if target not in words:
        return 0
    return bfs(begin, target, words)


def bfs(begin, target, words):
    
    q= deque()
    q.append((begin,0))
    visited = set()
    
    while(q):
        now, step = q.popleft()
        
        if now == target:
            return step
    
        #단어를 모두 체크, 해당 단어가 변경될 수 있는지 체크
        for word in words:
             if word not in visited:
                count = 0
                for i in range(len(now)): 
                    if now[i] != word[i]:
                          count+=1
            
                if count ==1:
                    visited.add(word)
                    q.append([word, step+1])
        
        
