# Day8 - Function Parameters and Caeser Cipher

def greet():
    print("Hello and welcome?")
    print("how are you?")
    print("thanks")

greet()


# Create a function that allows for input

"""
something = 123
    *        *
    *        *   
    *        *   
parametar  argument

"""


def greet_with_name(name):
    print(f"hello and welcome {name}")
    print(f"how are you {name}?")
    print("thanks")

greet_with_name("Angela")

# Function with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}. ")
    print(f"How is the weather in {location}.")

greet_with("Angela", "London")

# Function with keywords arguments

greet_with(name = "Angela", location = "London")




