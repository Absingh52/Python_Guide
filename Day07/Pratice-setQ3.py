# 4. Write a recursive function to calculate the sum of first n natural numbers
 
def fun(n):
    if(n==1):
        return 1
    return fun(n-1)+n  
  
n=int(input("enter the n:"))
result=fun(n)
print(result)