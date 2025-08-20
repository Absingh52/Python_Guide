# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function. 

name=input("Enter name :")
print(f"Good Afternoon {name}")

# 2. Write a program to fill in a letter template given below with name and date. 


letter = '''Dear <|Name|>,
 You are selected!
<|Date|> ''' 
print(letter.replace("<|Name|>","Abhishek").replace("<|Date|>","20/August/2025"))


# 3. Write a program to detect double space in a string.

statement="I am a good  boy "

print(statement.find("  "))

# 4. Replace the double space from problem 3 with single spaces. 

print(statement.replace("  "," "))