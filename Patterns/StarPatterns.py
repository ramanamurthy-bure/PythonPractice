print("############################## 1. Increased Triangle ##############################")
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=' ')
    print("")
print("############################## 2. Decreased Triangle ##############################")
n = 5
for i in range(n):
    for j in range(i,n):
        print("*", end=' ')
    print("")
print("############################## 3. Increase Triangle With Space and Decreased Triangle with * ##############################")
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n):
        print("*",end=' ')
    print("")
print("############################## 4. Increase Triangle With * and Decreased Triangle with space ##############################")
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,n-1):
        print("*",end=' ')
    for j in range(i,n):
        print("*",end=' ')
    print("")
