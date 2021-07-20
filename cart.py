
while True:
    

   product={"101":["samsung",20000,20],  "102":["Poco",30000,10],  "103":["Iphone",50000,7],  "104":["AsusLaptop",15000,40],  "105":["Mouse",1000,15]}
   cart={}
   
   ch=input("Enter your choice : 101.Samsung mobile 102.Poco Mobile 103.Iphone 104.Asus Laptop 105.Mouse").split()
   n=len(ch)
   print(f"You had entered {n} elements" )
   for a in ch:
      if a in product:
         qty=int(input("Enter the quantity : " ))
         if qty<=product[a][2]:
             pr=product[a][1]
             Price=qty*pr
             b=product[a][0],qty,Price
             cart.setdefault(a,b)
             print("Product added to cart successfully")
             print(cart)
         else:
             print("Invalid Quantity")
      else:
         print("Invalid Input")
   print("Enter the oprn to be done:1.Remove 2.update 3.View")
   choice=int(input())
   if choice == 1:
      ch=input("Enter the product id to be removed: 101.Samsung mobile 102.Poco Mobile 103.Iphone 104.Asus Laptop 105.Mouse")
          
      del cart[ch]
      print (cart)
   elif choice == 2:
       ch=input("Enter your choice : 101.Samsung mobile 102.Poco Mobile 103.Iphone 104.Asus Laptop 105.Mouse").split()
       n=len(ch)
       print(f"You had entered {n} elements" )
       for a in ch:
          if a in product:
             qty=int(input("Enter the quantity : " ))
             if qty<=product[a][2]:
                 pr=product[a][1]
                 Price=qty*pr
                 b=product[a][0],qty,Price
                 cart.setdefault(a,b)
                 print("Product added to cart successfully")
                 print(cart)
             else:
                 print("Invalid Quantity")
          else:
             print("Invalid Input")
   elif choice ==3:
      print(cart)
   else:
      print("print correct value")
      
          

