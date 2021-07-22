x=[]
n=int(input("Enter row value:  "))
#c=int(input("Enter col value:  "))
for i in range(n):
    x.append([])
    for j in range(n):
       x[i].append((int(input())))
for i in range(n):
    for j in range(n):
        if(((i==0 or i==n-1 or i==n//2) and j<=n-4) or j==0 or j==n-3):
            if x[i][j]<=9:
                print(" "+str(x[i][j]),end=" ")
            else:
                print(x[i][j],end=" ")
        else:
            print("  ",end=" ")
    print()
