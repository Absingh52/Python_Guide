# 2. Write a python program using function to convert Celsius to Fahrenheit.

# °F = (°C × 9/5) + 32

def fun(c):
    f=(c*9/5) +32
    return(f)

c=int(input("enter the temperature :"))
result=fun(c)
print(result)