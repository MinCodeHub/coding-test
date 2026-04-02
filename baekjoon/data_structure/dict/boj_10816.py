import sys

#dict 실습 
input = sys.stdin.readline

n = int(input())
card = input().split()

m = int(input())
findCard = input().split()

result = {}

for c in card:
    result[c] = result.get(c,0)+1

for f in findCard:
    print(result.get(f,0), end=" ")



# n = (int)(sys.stdin.readline().strip())

# card = sys.stdin.readline().split()

# m = (int)(sys.stdin.readline().strip())
    
# findCard = sys.stdin.readline().split()

# result ={}

# #카드 개수 세기
# for i in range(len(card)):
#   if(result.get(card[i])):
#      result[card[i]]+=1
#   else:
#     result[card[i]]=1
 
# #결과 출력
# for j in range(len(findCard)):
#     if(result.get(findCard[j])):
#         print(result[findCard[j]])
#     else:
#        print(0)