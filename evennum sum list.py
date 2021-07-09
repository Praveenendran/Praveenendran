
x=list(map(int,input().strip().split()))
sum=0
for i in range(len(x)):
    #x.append(int(input))
    if x[i]%2==0:
        sum=sum+x[i]
print(sum)
