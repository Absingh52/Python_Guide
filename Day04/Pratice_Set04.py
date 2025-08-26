# 1. Write a program to store seven fruits in a list entered by the user. 
li=["Apple","Mango","Banana","Orange","Graphes","WaterMelon","Guava"]
print(li)
li.pop(4)
print(li)

# 2. Write a program to accept marks of 6 students and display them in a sorted manner. 

marks=[]
s1=int(input("Enter the marks of student 1:"))
marks.append(s1)
s2=int(input("Enter the marks of student 2:"))
marks.append(s2)
s3=int(input("Enter the marks of student 3:"))
marks.append(s3)
s4=int(input("Enter the marks of student 4:"))
marks.append(s4)
s5=int(input("Enter the marks of student 5:"))
marks.append(s5)
print(marks)
print("sorted order")
marks.sort()
print(marks)

# 5. Write a program to count the number of zeros in the following tuple:
 
a = (7, 0, 8, 0, 0, 9) 
print(a.count(0))