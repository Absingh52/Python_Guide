# 1. Write a program to find the greatest of four numbers entered by the user. 
first=int(input("Enter the first number:"))
second=int(input("Enter the second number:"))
third=int(input("Enter the third  number:"))
fourth=int(input("Enter the fourth number:"))

if(first >= second and first >= third and first >= fourth ):
     print(first)
elif(second >=first and second>= third and second >= fourth ):
     print(second)
elif(third >= first and third>=second and third>=fourth):
     print(third)
else:
     print(fourth)
