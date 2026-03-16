a,b,c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
count = 0

for i in range(0,a):
    for j in range(0,b):
        for k in range(0,c):
            count+=1
            print(i,j,k,sep=" ")

print(count)