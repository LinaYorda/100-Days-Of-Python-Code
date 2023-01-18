# Python Loops


# For Loop - assigns a variables and lists every item on a list
# A loop alows us to execute the same line of code multiple times

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
    print(fruits)


# For Loop within a range function 

#for number in range(a,b): 
    #print(number)


for number in range(1, 11, 3):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)
