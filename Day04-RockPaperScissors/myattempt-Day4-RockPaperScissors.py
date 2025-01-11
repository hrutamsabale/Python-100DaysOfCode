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

list1=["rock","paper","scissors"]
user=input("What do you choose? ").lower()
input_index=list1.index(user)
if (input_index==0):
  print(f"You chose {rock}")
elif (input_index==1):
  print(f"You chose {paper}")
elif (input_index==2):
  print(f"You chose {scissors}")

computer_choice_index=random.randint(0,2)
computer_choice=list1[computer_choice_index]
if (computer_choice_index==0):
  print(f"PC chose {rock}")
elif (computer_choice_index==1):
  print(f"PC chose {paper}")
elif (computer_choice_index==2):
  print(f"PC chose {scissors}")

if(user=="rock"):
  if(computer_choice=="rock"):
    print("\nIt's a tie")
  elif(computer_choice=="paper"):
    print("\nYou lose")
  elif(computer_choice=="scissors"):
    print("\nYou win")
elif(user=="paper"):
  if(computer_choice=="rock"):
    print("\nYou win")
  elif(computer_choice=="paper"):
    print("\nIt's a tie")
  elif(computer_choice=="scissors"):
    print("\nYou lose")
elif(user=="scissors"):
  if(computer_choice=="rock"):
    print("\nYou lose")
  elif(computer_choice=="paper"):
    print("\nYou win")
  elif(computer_choice=="scissors"):
    print("\nIt's a tie")
  

