import random
rock = '''Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images=[rock,paper,scissors]
comp_choice=random.randint(0,2)
user_choice=int(input("What do you choose? 0: Rock, 1: Paper, 2: Scissors\n"))
if user_choice>2 or user_choice<0:
    print("\n\nInvalid Choice")
else:
    print(f"You Chose:\n{images[user_choice]}")
    print(f"\n\n\nComputer Chose:\n{images[comp_choice]}")
    if user_choice==comp_choice:
        print("\n\nIt's a DRAW")
    elif user_choice==0 and comp_choice==2:
        print("\n\nYou Win!")
    elif user_choice==2 and comp_choice==0:
        print("\n\nYou Lose")
    elif user_choice>comp_choice:
        print("\n\nYou Win!")
    elif comp_choice>user_choice:
        print("\n\nYou Lose")
