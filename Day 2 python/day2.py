# # Data Types
# print("hello"[4])
# name="hello"
# print(name[2])
# print("123"+"345")
# # integer
# 123 + 345
# print(123+345)
# # largeinteger
# 123_345_567
# #float
# 3.14159
# # boolean
# True
# False
# Your_name="SUMINLOVEISHA"
# print(Your_name[0]+Your_name[5]+Your_name[9])


# # changing data types
# num_char=len(input("what is your name"))
# new_num_char=str(num_char)
# print("your name has" +" " +new_num_char+" " + "characters")

# # ///////////////////////

# a=float(1414)
# print(type(a))
# print(70+float("100.5"))
# print(str(70)+str(100))






# TIP CALCULATOR
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome To Tip Calculator")
total_bill=float(input("what was the total bill??$"))
tip=int(input("WHat Percentage of tip would you like to give??10,12,15????"))
split=int(input("How many people to split the bill??"))
tip_as_int=float((tip/100)*total_bill)
total_amt_to_pay=total_bill+tip_as_int
Individual_pay=total_amt_to_pay/split
final_amount=round(Individual_pay,2)
print(f"EACH PERSON SHOULD PAY:${final_amount}")

