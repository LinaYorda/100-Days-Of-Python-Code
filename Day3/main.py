# Day3 - Control Flow and Logiacal Operators 

# conditional if / else statement

# if condition:
    #do this
# else:
    #do this


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride!")


# Nested if / else statment

# if condition:
    #if another condition:
    #   do this
    # else:
    # do that
# else:
#  #do that 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride a rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please, pay $7.")
    else:
        print("Please, pay $12. ")
else: 
    print("Sorry, you have to grow up taller before you can ride!")


# if / elif / else

# if condition1: 
    #do A
# elif condition2:
    # do B
# else:
    # do this


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please, pay $5.")
    elif age <= 18:
        bill = 7
        print("Please, pay $7.")
    else:
        bill = 12
        print("Please, pay $12.")
else: 
    print("Sorry, you have to grow taller before you can ride")


# Multiple if statements

print("Welcome to the rollercoaster!")
height = int(input("What is your height? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want a photo taken? Y or N ")

    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")



# Logical Operator A and B; C or D; not E

print("Welcome to the rollercoaster!")
height = int(input("What is your height? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    
    wants_photo = input("Do you want a photo taken? Y or N ")

    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")