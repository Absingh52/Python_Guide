# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Myclass:
    a=10

b=Myclass()
print(b.a)
b.a=0
print(b.a)
print(Myclass.a)