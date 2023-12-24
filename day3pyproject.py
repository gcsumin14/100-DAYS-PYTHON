#python project day 3
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1=input('You\'re are at cross roads,where do you wanna go??,Type "Left" or "Right"').lower() #here \ is a escape charcter which helped to print the statremente properly,if it was not there then 'you're will only be a string

if choice1.lower()=="left":
    #continue in the game.
    choice2=input('You\'ve come to a lake.There\'s a Island in the middle of the lake.Type "wait" to wait for a boat or Type "swim" to swim??\n')
    if choice2.lower()=="wait":
        #game will continue
        choice3=input('You arrived at the island unharmed,There is a house with three doors.one red,one yellow and one blue.which color do you choose??').lower()
        if choice3=="red":
            print("It\'s a room full of fire.Game over")
        elif choice3=="yellow":
            print("You found a treasure!!You win") 
        elif choice3=="blue":
            print("You entered a room of freaking beasts,game over")
        else:
            print("You chose a door that doesn\'t exists.Game over")
    else:
        print("You got attacked by a angry trout.Game Over")
else:
    print("Game Over!!cuz you fell into a hole")

