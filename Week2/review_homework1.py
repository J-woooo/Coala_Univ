line = int(input("줄 수를 입력하세요: "))
# mid = int(line / 2) + 1

for i in range(0,line+1):
    for j in range(0,i):
        print("*",end='')
    print("")
for i in range(line-1,0,-1):
    for j in range(0,i):
        print("*",end='')
    print("")