
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

game_images = [rock, paper, scissors]
choice_computer = random.randint(0,2)

what_do_you_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))



if  int(what_do_you_chose) >= 3 or int(what_do_you_chose)< 0: 
       print("You typed an invalid number and you lose")

else:

    print(game_images[what_do_you_chose])
    choice_computer = random.randint(0,2)
    print("Computer chose: ")
    print(game_images[choice_computer])
    if int(what_do_you_chose) == 0 and int(choice_computer) == 2: 
        print("You win!")
    
    elif int(what_do_you_chose) >= 3 or int(what_do_you_chose)< 0: 
       print("You typed an invalid number and you lose")

    elif int(what_do_you_chose) > int(choice_computer):
        print("you lose")
    
    elif int(what_do_you_chose) == int(choice_computer):
        print("That is a draw")

    elif int(choice_computer) > int(what_do_you_chose):
        print("You lose!")

    elif int(what_do_you_chose) > int(choice_computer):
        print("You win!")


