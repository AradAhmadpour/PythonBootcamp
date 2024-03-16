# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)
height_sum = 0
users_num = 0
# 🚨 Don't change the code above 👆
for height in student_heights:
  height_sum += height
  users_num += 1

avg= height_sum / users_num 
print(avg)

#Write your code below this row 👇




