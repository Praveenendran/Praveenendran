n= int(input("Enter a number : "))
a=0
t=n
while t!=0:
    i=t%10
    a=a+(i**3)              
    t=t//10
if a==n:
    print(f"Number is amstrong number and the value is {a}")
else:
    print(f"{a} is not an anstrong number")
    
