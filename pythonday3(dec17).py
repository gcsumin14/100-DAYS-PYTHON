# BMI 2.0
# Enter your height in meters e.g., 1.55
height = float(input("ENTER YOUR HEIGHT IN M: "))
# Enter your weight in kilograms e.g., 72
weight = int(input("ENTER YOUR WEIGHT IN KG: "))
# 🚨 Don't change the code above 👆


# Write your code below this line 👇
BMI = weight / height**2

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif 18.5 <= BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif 25 <= BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif 30 <= BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
