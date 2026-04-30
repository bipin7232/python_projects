def febini():
    num = int(input("Enter a number: "))

    firstNum= 0
    secondNum = 1

    for i in range(num):
        print(firstNum, end=" ")
        lastnum = firstNum + secondNum
      

        firstNum = secondNum
        secondNum = lastnum

febini()
