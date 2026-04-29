def febini():
    num = int(input("Enter a number: "))

    firstNum= 0
    secondNum = 1

    for i in range(num):
        lastnum = firstNum + secondNum
        print(lastnum, end=" ")

        firstNum = secondNum
        secondNum = lastnum

febini()
