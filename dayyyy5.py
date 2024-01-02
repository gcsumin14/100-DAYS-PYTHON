#to calculate the highest number from a list of numbers
list=input("LIST OF NUMBERS:\n").split()
for n in range(0,len(list)):
    list[n]=int(list[n])
highest_score=0
for score in list:
    if score>highest_score:
        highest_score=score
        print(f"The Highest Score is; {highest_score}")
