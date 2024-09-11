
def pattern(n):
    for i in range(0,4):
        for j in range(0,i):
            print(" ", end=" ")
        for j in range(i,n):
            print("*",end=" ")
        print()



n = 4
output = pattern(n)