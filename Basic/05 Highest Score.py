# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
highest_score = 0
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
for student in student_scores:
  if student > highest_score:
    highest_score = student
print(highest_score)


