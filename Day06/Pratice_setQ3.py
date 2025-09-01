# 5. Write a program to find the sum of first n natural numbers using while loop.

n=int(input("Enter the value of n:"))
sum=0
i=1
while(i<=n):
    sum+=i
    i+=1

print("sum of first n natural numbers :",sum)