#반복문(for)과 range 연습하기

#1부터 10까지 별찍기
print("1부터 10까지 별찍기")
for i in range(1,11):
    for j in range(1,i+1):
        print("*",end='')
    print("")
print("")

#1부터 2칸씩 별찍기
print("1부터 2칸씩 별찍기")
for i in range(1,11,2):
    for j in range(1,i+1):
        print("*",end='')
    print("")
print("")

#10부터 1까지 별찍기
print("10부터 1까지 별찍기")
for i in range(10,0,-1):
    for j in range(0,i):
        print("*",end='')
    print("")
print("")