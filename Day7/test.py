import random

word_list =["aardvik", "baboon", "camil"]
display = []

chosen_word = random.choice(word_list)
guess = input("Make a guess: ").lower()

for letter in chosen_word:
    
    if letter == guess:
        print("Right")
    else:
        print("Wrong")