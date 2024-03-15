import random

# Get Persons name from user
names_input = input("Write Everybody's name and seperate them with a comma :")
names= names_input.split(",")

# Pick a random name | path 1
nameslist_count = len(names)
random_num = random.randint(0, nameslist_count -1)
random_name = names[random_num]

# pick a random name | path 2
random_name = random.choice(names)

# Show payer name
print(f"{random_name} should pay the bill today!")