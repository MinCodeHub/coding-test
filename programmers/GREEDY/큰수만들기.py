def solution(number, k):
    
    # prev : 이전 값
    # 이전 값보다 크면 list에 넣기
    # 이전 값보다 작으면 list에 넣지말고 cnt증가 시키기
    # -> 이전값하고만 비교하면 안됨.
    #스택을 사용해서 풀어야함
    stack = []
    
    for num in number:       
        while (k > 0 and stack and stack[-1] < num):
            stack.pop() #스택의 마지막 값이 현재 값보다 작으면 stack에서 없앰
            k-=1
        stack.append(num)
        
    if k > 0: #k가 남아있으면 뒤에서 잘라야함.
        stack = stack[:-k] #리스트 뒤에서 k개 잘라버린다
    
    return ''.join(stack)