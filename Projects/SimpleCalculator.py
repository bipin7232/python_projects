def calculator():
    number1 = int(input("Enter a number : "))
    number2 = int(input("Enter a number : "))

    cal = ["add","subtract","division","multiply"]
    print(cal)
    show = int(input("enter what you want(enter number) : "))

    if(show==1):
        print ("add: ",number1 + number2)
    elif(show==2):
        print("sub",number1-number2)
    elif(show==3):
        print("division",number1/number2)
    elif(show==4):
        print("multiply",number1*number2)
    else:
        print("enter poper number")


calculator()
