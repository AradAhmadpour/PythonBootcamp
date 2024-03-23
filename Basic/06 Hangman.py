import random
words_list = ["arad", "ava", "asghar", "jafar"]

# Chose a random word
display_word = []
chosen_word = random.choice(words_list)
print(f"Random word is {chosen_word}")
display_word = ["_" for letter in chosen_word]
print (display_word)

# Ask user to guess a letter and lowercase it
guess = (input("Please enter a letter: ")).lower()
print(guess)

# Is the letter in chosen word?
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display_word[position] = guess
print (display_word)