# Getting Data From User
age= input("what is your current age? ")
dead_age = input("How many years do you want to live? ")

# Convert Inputs to int
int_age= int(age)
int_dead_age= int(dead_age)

# Caculate Dead Age Years, Weeks and Months
dead_age_years= int_dead_age
dead_age_months= int_dead_age * 12
dead_age_weeks= int_dead_age * 52
dead_age_days= int_dead_age * 365

# Caculate Current Age Years, Weeks and Months
age_years= int_age
age_months= int_age * 12
age_weeks= int_age * 52
age_days= int_age * 365

# Life Left Caculation
years_left= dead_age_years- age_years
months_left= dead_age_months- age_months
weeks_left= dead_age_weeks- age_weeks
days_left= dead_age_days- age_days

# Print Caculations
life_left= (f"You have {years_left} Years Left Which means;\nyou have {days_left} Days, {weeks_left} weeks, and {months_left} months left.")
print(life_left)