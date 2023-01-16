# Day4 - Randomisation and Python Lists

# Radomisation - random = module, created by Python team
import random
random_integer = random.randint(1, 10)
print(random_integer)

# floating number

import random
random_float = random.random()
print(random_float)

# random decimal number between 0 and 5? 

import random
random_decimal = random.randint(0, 5)
print(random_decimal)


# LISTS - the first number always starts at 0; 

# fruits = [item1, item2]
# fruits = ["Cherry", "Apple", "Pear"]

states_of_america = ["Delware", "Pennsylvania", "New York"]

print(states_of_america[2])

    # using negative index (-1)

print(states_of_america[-2])

    # change things

states_of_america[1] = "Pencilvania"
print(states_of_america)

    # add an item - append function

states_of_america.append("Angelaland")
print(states_of_america)

    # extend function - add more items on the list

states_of_america.extend(["Angelaland", "Jack Bauer Land"])
print(states_of_america)


# Index Errors and working with Nested Lists

num_of_states = len(states_of_america)
print(states_of_america[num_of_states - 1])

    # Nested Lists

dirty_dozen = ["Strawberries", "Spinach", "kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarine", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[0])
print(dirty_dozen[1])

print(dirty_dozen[1][2])
print(dirty_dozen[1][3])
print(dirty_dozen[1][1])







