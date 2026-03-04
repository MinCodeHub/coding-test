a = input()
a = int(a)

if(a == 12 or a== 1 or a ==2):
    print("winter")
elif(a ==3 or a == 4 or a== 5):
    print("spring")
elif(a == 6 or a== 7 or a ==8):
    print("summer")
else:
    print("fall")

# in을 쓰면 더 간단

# if a in [12, 1, 2]:
#     print("winter")
# elif a in [3, 4, 5]:
#     print("spring")
# elif a in [6, 7, 8]:
#     print("summer")
# else:
#     print("fall")