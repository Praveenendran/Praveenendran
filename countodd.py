x=list(map(int,input().strip().split()))
t=0
for i in range(len(x)):
    if x[i]%2==1:
        t=t+1
print(t)
    
