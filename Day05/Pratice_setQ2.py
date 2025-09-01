# 2. Write a program to find out whether a student has passed or failed if it requires a total 
# of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 

subject1=float(input("Enter the marks in maths:"))
subject2=float(input("Enter the marks in english:"))
subject3=float(input("Enter the marks in science :"))
sum=subject1+subject2+subject3
percentage=(sum*100)/300

if(percentage<33):
    print("fail")
    print("percentage is",round(percentage,2),"%")
else:
    print("pass")
    print("percentage is",round(percentage,2),"%")

