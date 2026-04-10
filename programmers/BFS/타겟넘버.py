from collections import deque;

def solution(numbers, target):
    
    q = deque();
    q.append((0,0))
    cnt = 0
    total1 = 0
    total2 = 0
    
    while(q):
        
        total, idx = q.popleft()
        
          
        if idx == (len(numbers)) :
            if (total == target):
                cnt+=1
            continue  
    
        total1 = total + numbers[idx] * (-1)
        total2 = total+ numbers[idx] * (1)
        q.append((total1, idx+1))
        q.append((total2, idx+1))
            
            
    return cnt