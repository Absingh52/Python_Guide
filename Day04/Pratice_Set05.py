# this introduction to dictionary

# intro={
#     "first name":"Abhishek",
#     "last name":"singh",
#     "roll number":4552,
#     "age":21
# }
# print("Printing Keys =",intro.keys())
# print("Printing values=",intro.values())
# print("Printing both=",intro.items())
# intro["department"]=["BCA"]
# print("Printing intro=",intro)
# del intro["age"]
# print("After deleting age from  intro=",intro)
# print("Update function()")
# intro.update({"age":"20","department":"bachelor of applications"})
# print("after update",intro)

# set
# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).
# empty_set=set()
# e1=int(input("enter digit:"))
# empty_set.add(e1)
# e2=int(input("enter digit:"))
# empty_set.add(e2)
# e3=int(input("enter digit:"))
# empty_set.add(e3)
# e4=int(input("enter digit:"))
# empty_set.add(e4)
# e5=int(input("enter digit:"))
# empty_set.add(e5)
# e6=int(input("enter digit:"))
# empty_set.add(e6)
# e7=int(input("enter digit:"))
# empty_set.add(e7)
# e8=int(input("enter digit:"))
# empty_set.add(e8)
# empty_set.add(18)
# empty_set.add('18')
# print("this is set ",empty_set)

# # 4. What will be the length of following set s: 
s = set()
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations? 
print(len(s))