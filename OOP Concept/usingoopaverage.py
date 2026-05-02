class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    

    def average(self):
        sum = 0
        for value in self.marks:
            sum += value

        print("hi ", self.name, "your marks is ", sum/3)
        
    


s1 = Student("bipin",[2,3,4])
s1.average()




        

