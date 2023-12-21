# IF+NESTED if+multiple if
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
if height >=120:
  print("you can ride rollercoaster")
  age=int(input("what is your age???"))
  if age<12:
    bill=5
    print("child tickets are 5$")
  elif age<=18:
    bill=7
    print("youth tickets are 7$")
  elif age>=45 and age<=55:
    print("CONGRATS,YOU HAVE A FREE RIDE")
  else:
    bill=12
    print("Adults tickets are 12$")
    wants_photo=input("Do you want a photo taken or not??Y or N??")
    if wants_photo.lower()=="y":
      bill=bill+3
      print(f"your Final BIll is {bill}$")
   
    else:
      print(f"ENJOY!!,YOUR BILL IS {bill}$")
  
else:
  print("Sorry,you cannot ride rollercoaster")
  