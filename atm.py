print("Welcome to XYZ Bank")
pin = int(input("Please enter your 4 digit number...."))
Bal=30000
if pin>=1000 and pin<=9999:
    print("please choose any one option below......")
    print("1. Deposit 2. Withdraw 3. Balane Enquiry ")
    value=int(input())
    if value == 1:
        Ru=int(input("Please enter the amount to be deposited : "))
        if Ru>0 and Ru<=20000: 
            print(f"u have deposited rupees {Ru} and your account balance is{Ru+Bal}")
        else:
            print("Deposit amount limited to 20000 Rs, Please Try again")
    elif value == 2:
        Ru=int(input("Please enter the amount to be withdrawed : "))
        if Ru>0 and Ru<=20000:
            print(f"u have withdrawn rupees {Ru} and your account balance is{Bal-Ru}")
        else:
            print("Withdrawl amount limited to 20000 Rs, Please Try again")
    elif value == 3 :
        print(f"Ur account balance is {Bal}")
else:
    print("invalid PIN")
