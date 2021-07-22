x=[]
n=int(input("Enter value:  "))

for i in range(n):
    x.append([])
    for j in range(n):
       x[i].append((int(input())))
for i in range(n):
    for j in range(n):
        if ((i==0 and j<n-2) or (i==n-1 and j<n-2) or (i==n//2 and j<n-2 )) or((j==0 and i<n//2)or(j==n-3 and i>n//2) ):
            if x[i][j]<=9:
                print(" "+str(x[i][j]),end=" ")
            else:
                print(x[i][j],end=" ")
        else:
            print("  ",end=" ")
    print()
