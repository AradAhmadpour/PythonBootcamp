import random

# Find out user choice
print(" Be bazi Sang Kaghaz Keghchi Khosh Amadid!")
i=1
while i == 1:
    user_choice = input('Entekhab konid, "sang" "kaghaz" ya "gheichi": ')
    print (f'Entekhab Shome :{user_choice}')
    if user_choice == "sang":
        print('''    _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    ''')
        
    if user_choice == "kaghaz":
        print('''    _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    ''')
        
    if user_choice == "gheichi":
        print('''    _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)''')

    # Find out CPU choice
    posibble_choices = ["sang","kaghaz","gheichi"]
    cpu_choice = random.choice(posibble_choices)
    print (f'Computer: {cpu_choice}')
    if cpu_choice == "sang":
        print('''    _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    ''')
        
    if cpu_choice == "kaghaz":
        print('''    _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    ''')
        
    if cpu_choice == "gheichi":
        print('''    _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)''')

    # Game Rules
    if user_choice == "sang":
        if cpu_choice == "sang":
            print("Mosavi Shodi! 😶")
        elif cpu_choice == "kaghaz":
            print("Bakhti! 😢")
        else:
            print("Bordi! 🥳")
    if user_choice == "kaghaz":
        if cpu_choice == "sang":
            print("Bordi! 🥳")
        elif cpu_choice == "kaghaz":
            print("Mosavi Shodi! 😶")
        else:
            print("Bakhti! 😢")
    if user_choice == "gheichi":
        if cpu_choice == "sang":
            print("Bakhti! 😢")
        elif cpu_choice == "kaghaz":
            print("Bordi! 🥳")
        else:
            print("Mosavi Shodi! 😶")