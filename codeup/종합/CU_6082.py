n = int(input())
for i in range(1,n+1):
    num = i
    count = 0
    while(num > 0):
        if num % 10 in [3,6,9]:
            count+=1
        
        num //= 10
    
    if count > 0:
            print("X"*count, end=' ')
    else:
        print(i, end=' ')