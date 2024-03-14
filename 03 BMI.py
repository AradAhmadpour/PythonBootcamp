print("BMI Caculator")

# Get data from user
weight = float(input("Enter your weight (Kg): "))
height = float(input("Enter your height (m): "))

# Caculate BMI
BMI = weight / (height ** 2)

# Show Data to User
if BMI < 18.5:
    print(f'Your BMI number is {BMI} and you are UNDER WEIGHT')
elif BMI < 25:
    print(f'Your BMI number is {BMI} and you have NORMAL WEIGHT')
elif BMI < 30:
    print(f'Your BMI number is {BMI} and you are OVER WEIGHT')
elif BMI < 35:
    print(f'Your BMI number is {BMI} and you are OBESE')
else:
    print(f'Your BMI number is {BMI} and you CLINICALLY OBESE')