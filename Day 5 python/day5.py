# #for loop
# fruits=["apple","peach","banana"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " " + "pie")
# print(fruits)
# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height=0
for height in student_heights:
  total_height+=height
print(f"Total height = {total_height}")
number_of_students=0
for students in student_heights:
  number_of_students+=1
print(f"Number of Students = {number_of_students}")
average_height= round(total_height/number_of_students,2)
print(f"Average Height= {average_height}")
