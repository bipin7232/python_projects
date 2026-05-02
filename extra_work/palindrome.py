x = int(input("Enter the number : "))
orginal = x

rev = 0

while x != 0:
    rem = x %10
    rev = rev *10 + rem
    x = x //10

if(rev == orginal):
        print("palindrome")
else:
        print("not palindrome")