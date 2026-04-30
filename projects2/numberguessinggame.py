import random

number = random.randint(0,100)
print(number)

while True:
  guess = int(input("Guess the number: "))
  if(guess==number):
   print("Right number")
   break
  
   print("Too high")
   break
  elif(guess<number):
    print("Too low")
    
  elif(guess>number):
    print("Too high")
  else:
    print("Enter the Valid number")