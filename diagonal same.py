a=int(input("Enter number 1 :"))
b=int(input("Enter number 2 :"))
x= a//10
y= b%10
x1= a%10
y1= b//10
if x==y:
   if x1==y1:
        print(f"{x} is True , {y} is True")
   elif x1!=y1:
        print(f"{x} is True , {y} is False")
elif x!=y:
    if x1==y1:
        print(f"{x} is False , {y} is True")
    elif x1!=y1:
        print(f"{x} is False , {y} is False")
