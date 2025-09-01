# 4. Write a program to find whether a given username contains less than 10
# characters or not.

userName=input("Enter the user name:")

if(len(userName)<10):
    print("it contain less than 10 characters")
else:
    print("NOT!")