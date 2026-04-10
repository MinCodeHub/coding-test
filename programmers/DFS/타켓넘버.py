#dfs
def solution(numbers, target):
    cnt = 0
    
    def dfs(idx, total):
        #종료 조건
        if idx == len(numbers):
            return 1 if total == target else 0
        
        plus = dfs(idx+1, total+numbers[idx])
        minus = dfs(idx+1, total-numbers[idx])
        
        return plus+ minus
    return dfs(0,0)