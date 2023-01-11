## Data Types in Python 

# Strings - counting character starts always at 0; Python treats everything inside "" as a string

print("Hello"[0])

# Integer - a whole number without decimal (positive or negative)

print(123 + 345)

# Float = Floating Point Number; examle - 3.14159

# Boolean - tests is something is True or False

True
False

# Type Error, Type Checking and Type Conversion

# Code below will produce a TypeError: can only concatenate str (not "int") to str
# num_char = len(input("What is your name? "))
# print("Your name has " + num_char + "character.")

# but 

# we can use a fuction called type, so to check what kind of data is - <class 'int'>

# function type()

num_char = len(input("What is your name? "))
print(type(num_char))

# function str() - converts an integer to a string so our code wont break

num_char = len(input("What is your name? "))
num_char_new = str(num_char)
print("Your name has " + num_char_new + " character.")

a = 123
print(type(a))

# print(70 + float("100.5"))

print(str(70) + str(100))

# Mathematical operations in Python 

print(3 + 5)
print(7 - 4)
print(3 * 2)
print(6 / 3)
print(2 ** 3)

    # PEMDASR Rule - Parentheses()/ Exponents**/Multiplication*/Division//Addition+/Substraction-

# round() 

print(round(8 / 3, 2))

# flow division 

print(8 // 3)

result = 4 / 2
result /= 2
print(result)

# /*+-=

score = 0
score -= 1
print(score)

# f-string - 

score = 0
height = 1.8
isWinning = True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning} ")










