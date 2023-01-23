# Functions, Code Blocks and While Loops


print("Hello")
num = len("Hello")
print(num)

# creating my own function:

"""
def my_function():
    #Do this
    #Then do this
    Finally do this
"""

def my_function():
    print("Hello")
    print("Goodbye")

my_function()

# Indentation 

"""
def my_function():
    print("Hello")

print("world)

"""

# While Loop 
# while something_is_true:


# Reeborg's World. Find more games at http://reeborg.ca/reeborg.html 

    ## Hurdle 1

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()

"""

# Hurdle 2

"""
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for step in range(6):
    jump()
    
"""
# While Loop
"""
number_of_hurdles = 6

while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    
"""    
"""    
initial_move()
top_move()
initial_move()
top_move()
initial_move()
top_move()
initial_move()
top_move()
initial_move()
top_move()
initial_move()
top_move()
"""

"""
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
    jump()
"""     

# While Loop

"""
while at_goal() != True:
    jump()
    
"""   
# Hurdle3

"""
while at_goal() != True: 
    if wall_in_front() == True:
        jump()
    else: 
        move()
    
""" 

# Hurdle 4
"""
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is clear():
        move()
    turn_left()


while at_goal() != True:
    if wall_in_front() == True:
        jump()
    else:
        move()

"""

# Maze

"""
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else: 
        turn_left()
"""