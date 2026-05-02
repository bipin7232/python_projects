def is_leapyear(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("leap")
        
    else:
        print("not leap")

year = int(input("enter the year: "))
is_leapyear(year)