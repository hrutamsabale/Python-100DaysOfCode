import random
chosen_number=random.randint(1,100)
def difficulty():
  difficulty=input("Choose a difficulty, 'Hard' or 'Easy': ").lower()
  if difficulty=='easy':
    attempts=10
  elif difficulty=='hard':
    attempts=5
  else:
    print("Invalid Choice")
    attempts=0
  return attempts
attempts=difficulty()
def chose_number():
  global attempts
  print(f"\nYou've got {attempts} attempts")
  user_number=int(input("Enter a number: "))
  if user_number==chosen_number:
    print(f"\nYou Won!. The answer was indeed {chosen_number}.")
    attempts=-1
  elif user_number<chosen_number:
    print("Too Low")
    attempts-=1
  else:
    print("Too High")
    attempts-=1
while(attempts>0):
  chose_number()
  if attempts==0:
    print(f"\nGame Over. The answer was {chosen_number}")
  elif attempts==-1:
    print("Game Over.")
  else:
    print("Guess Again")
