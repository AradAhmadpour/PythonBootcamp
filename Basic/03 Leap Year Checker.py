print("Leap Year Checker")
year = int(input("Enter the year you want to check: "))

# Checking if the year ir a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year')
        else:
            print(f'{year} is not a leap year')
    else:
        print(f'{year} is a leap year')

else:
    print(f'{year} is not a leap year')