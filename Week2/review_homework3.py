# 1 oooo*oooo   4
# 3 ooo***ooo   3~5
# 5 oo*****oo   
# 7 o*******o   1234567
# 9 *********   012345678
size = 4
k=1
for i in range(0,5):
    for j in range(0,9):
        if(j<=size-k or j>=size+k):
            print(" ",end="")
        else:
            print("*",end="") 
    print("")
    k+=1