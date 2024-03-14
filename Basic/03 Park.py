print("welcome to Arad Park")

# Get Data from user
name = input("Enter your name: ")
height = int(input("Enter your height: "))
bill = 0

# Checking user data
if height >=120:
    print(f'You can ride roller coaster')
    age = int(input(f"Now Enter your age {name}: "))
    if age < 12:
        bill = 5
        print(f'{name},please pay ${bill}')
    elif age <= 18:
        bill = 9
        print(f'{name},please pay ${bill}')
    elif age >= 45 and age <=55:
        print(f'Congratulations {name}!,Your Ticket is FREE!')
    else:
        bill = 12
        print(f'{name},please pay ${bill}')
    take_photo = input("Do you want to take a photo? Y / N ")
    if take_photo == "Y":
        bill += 3
        print(f"your finall bill is ${bill}")
    else:
        print("OK, Hope you enjoy!")
else:
    print(f"sorry, {name} unfortunately you can't ride roller coaster now. We will wait for you to grow more :)")