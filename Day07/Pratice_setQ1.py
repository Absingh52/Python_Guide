# 1. Write a program using functions to find greatest of three numbers.

def fuc(a,b,c):
    if(a>b and a>c):
       return("a is greatest")
    elif(b>a and b>c):
        return("b is greatest")
    else:
        return("c is greatest ")


a=int(input("enter the a :"))
b=int(input("enter the b :"))
c=int(input("enter the c :"))

result=fuc(a,b,c)

print(result)
