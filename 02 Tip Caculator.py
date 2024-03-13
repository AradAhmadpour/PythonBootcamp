# Getting Data From User
print("Welcome to Tip Caculator")
Total_Bill= float(input("What wat the total bill? "))
Tip_Percentage= int(input("what percentage tip would you like to give?"))
People= int(input("How many people to split the bill? "))

# Convert Tip Percentage to num
Tip_Percentage_num = (1 + Tip_Percentage/100)

# Caculation
Tip_price= ((Total_Bill / People) * Tip_Percentage_num)
Final_amount= (round(Tip_price, 2))
print(f"Each Person should pay {Final_amount}")