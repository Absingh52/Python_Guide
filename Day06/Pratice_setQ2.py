# 4. Write a program to find whether a given number is prime or not
a=int(input("enter the number :"))

if (a<=1):
    print("Not a prime Number")

Is_prime=True
for i in range(2,int(a**0.5)+1):
    if(a%i==0):
        Is_prime=False
        break

if Is_prime:
    print("Prime")
else:
    print("NOt Prime")

