class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student")

s1 = Student("bipin",99)
print(s1.name,s1.marks)

s2 = Student("ram",100)
print(s2.name, s2.marks)
