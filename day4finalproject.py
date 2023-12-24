#rock paper scissors= 0 for rock 1 for paper 2 for scissors 
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[rock,paper,scissors]
you_choose=int(input("What do you choose??0 for ROCK 1 for PAPER 2 for SCISSORS:\n"))
if you_choose>=3 or you_choose<0:
    print("You Typed An Invalid Number")
else:
    print(game_images[you_choose])
    print("COMPUTER CHOSE:")
    random_comp=random.randint(0,2)
    print(game_images[random_comp])
    if you_choose==0 and random_comp==2:
        print("YOU WIN!!")
    elif you_choose==2 and random_comp==0:
        print("YOU LOSE!!")
    elif random_comp>you_choose:
        print("YOU LOSE!!")
    elif you_choose>random_comp:
        print("YOU WIN!!")
    elif you_choose==random_comp:
        print("IT\'s A DRAW!!")
# if you_choose==0:
#     print(rock)
# elif you_choose==1:
#     print(paper)
# elif you_choose==2:
#     print(scissors)
# else:
#     print("RETRY")


# if random_comp==0:
#     print("""
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """)
# elif random_comp==1:
#     print("""
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """)
# elif random_comp==2:
#     print("""
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# """)
# elif you_choose>2:
#     print("RETRY")
# if you_choose==1 and random_comp==0:
#     print("You Win")
# elif you_choose==0 and random_comp==2:
#     print("You win")
# elif you_choose==2 and random_comp==1:
#     print("You Win")
# elif you_choose==0 and random_comp==1:
#     print("You lose")
# elif you_choose==2 and random_comp==0:
#     print("You lose")
# elif you_choose==1 and random_comp==2:
#     print("You lose")
# else:
#     print("Draw")


..

