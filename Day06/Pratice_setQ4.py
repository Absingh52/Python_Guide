# 6. Write a program to calculate the factorial of a given number using for loop.


n=int(input("Enter the value of n:"))
fact=1
i=1
while(i<=n):
   fact*=i
   i+=1

print("factorial of given number  :",fact)