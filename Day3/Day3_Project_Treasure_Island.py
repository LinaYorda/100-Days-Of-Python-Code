# Day 3 Project: Treasure Island

print('''



            ]=[
          .'   `.             `.-v-.'
.-._.._  /_______\ ..--.`-._
       `-|  .---.|          `--.._                    `.-v-.'
         |  |.-.||           _..--`
 `.-o-.' |  |'-'||     _..--`               `.-o-.'
     .-..|  '---'|..--`                              .--.
-._.`   _|..---..|_                                .`    `-._
       |__..---..__|                              `--.._     `--.._
        |  _ | |_||     `.-v-.'          `.-v-.'        `--.._     `.
        | |_||   _|                                           `--..`
      __|_..---.._|__
     |___...---...___|
      |  _   |     _|              `.-o-.'
      | | | _| _    |
      | |_|  |    _ |      _....--```.                       `.-v-.'
      | _    |   | ||..--``     ..-..`          `.-o-.'
   _..|   _  |_  |_||       ..``
 -`   |  | | |    _ |   _.-`
      |  |_| |  _   |.-`             __       __
      | _    | | |  |                ||       ||
  .--`|  _   | |_|  |        ________||_______||
      | | | _|     _|       /_ _ _ _/ \\_ _ _/ \\
      | | |  | _    |      /_ _ _ _/   \\_ _/ _ \\
      |__...---...__|     /_ _ _ _/_   _\\ / | | \\   `.::::::::::::::::::
  _..-'__...---...__'-._ /_ _ _ _/| | | |\\  |_| |\\    `-._::::::::::::::
 |_..-'      |  _   '-._/_______/ |_| |_| \\    _|          `.::::::::::::
  | _      _ |       _  |   _  |_ _ _ _ _ _ _ _ _|   .,       `-.:::::::::
  |     _    | _        |  _   |_|_|_|_|_|_|_|_|_|         ,.    `.:::::::
  |  _      _|     _    | | | -| _           _   |  .,             `.:::::
  |_.   .-._ | _       _| | |  |      _   _______|_             .,   `-.::
-'   `-'    `'._.`-._.--'`--.._|  _      /_ _ _ _ /\    ,.           ,. `.
`...    .,                   ., `-._  _ / _ _ _ _/ -\                 _.-
    `.           ,.      .,         `-./_ _ _ _ /  _ \      ,.    _.-`::::
    .'     ,.                          `-. ____/| |_||\        .-'::::::::
 _.'                                ,.    `-.  -|   _|       .':::::::::::
             .,       ,.                     `. |-__ | .,  .':::::::::::::
                                 ,.            \||  ||   .-'::::::::::::::
     .,                    ,.            ,.     ||  || .':::::::::::::::::
                  .,                       __.--.:::::':::::::::::::::::::
LGB    _.-``-._=:..-_.,=`:;.,-=.'-._..---``..:::::::::::::::::::::::::::::
``--..` ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
''')

print("Welcome to Tresure Island!")
print("Your mission is to find the tresure.")
choice_one = input('You are at a crossroad, where do you want to go? Type "left" or "right". ')
choice_one = choice_one.lower()

if choice_one == "left":
    choice_two = input('You have come across to a lake. There is a island in the midddle. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()

    if choice_two == "wait": 
        choice_three = input("You arrive at the island ungarmed. There is a house with 3 doors.One red, one yellow and one blue. Which colour do you choose?").lower()

        if choice_three == "red":
            print("It is aroom full of fire. Game Over.")
        elif choice_three == "yellow":
            print("You found the treasure! You win!")
        elif choice_three == "blue":
            print("You enter a room of beasts. Game over.")
        else: 
            print("You chose a door that doesnt exist. Game Over!")
    else: 
        print("You got attacked by an angry trout. Game Over")
else: 
    print("You fell into a hole. Game Over")