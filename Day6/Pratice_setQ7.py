# 7. Write a program to print the following star pattern.
#  *
# ***
# ***** for 
n =int(input("Enter the value of n:"))

for i in range(1,n+1):
    print(" "* (n-i),end="")
    print("*"* (2*i-1),end="")
    print("")
        
#     8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3

for i in range(1,n+1):
    print("*"* (i),end="")
    print("")

# 9. Write a program to print the following star pattern.
# * * *
# *   * for n = 3
# * * * 
print("")
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*" * (1*n),end="")
        print("")
    else:
        print("*",end="")
        print(" "* (n-2),end="")
        print("*",end="")
        print("")