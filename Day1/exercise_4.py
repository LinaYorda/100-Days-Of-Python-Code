# Exercise 4 - Variables

# write a program that switches the value stored in a variables a and b. 

# Example Input a: 3, b: 5
# Example Output a: 5, b: 3


a = input("a: ")
b = input("b: ")

# introducing a new variable c 

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)
