def missingnumber():
    nums = int(input("Enter the number(start 0 ): " ))
    n = nums
    for i in range(0,10):
        if(i!=n):
            print(i)

        else:
            print("done")

missingnumber()