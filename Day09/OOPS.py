#  concept of OOPs in python 

# class
class Student:
    # class variable
    college="Dronacharya college "

    # constructor
    def __init__(self,name="Unkown",age="none",rollno="none"):
        self.name=name
        self.age=age
        self.rollno=rollno
        print("This Constructor!")
    
    # method
    def PrintOutput(self):
        print(f"Name:{self.name}, Age:{self.age},RollNo:{self.rollno},{self.college}")


# objects
Student4=Student.college
Student1=Student("Abhishek",21,4552)
Student2=Student("Dhruv",20,4542)
Student3=Student("Priyanshu",20,4567)
          
Student1.PrintOutput()
Student2.PrintOutput()
Student3.PrintOutput()
