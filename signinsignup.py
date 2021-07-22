user={}
while True:
    ch=int(input("1.Sign Up 2.Sign in 3.Exit"))
    if ch==1:
        uname=input("User Input : ")
        email=input("email : ")
        mobile=input("mobile : ")
        password=input("password : ")
        user={uname:(email,mobile, password)}
        if uname in user:
           print("username already exist")
        else:
           print("Account already added")
    elif ch == 2:
        uname=input("username : ") 
        password=input("password : ")
        if(((uname in user) or (email in user[uname][0])) and (password in user[uname][2])):
            print("Login successful")
        else:
            print("invalid Password.Please try again")
    else:
        break






            
