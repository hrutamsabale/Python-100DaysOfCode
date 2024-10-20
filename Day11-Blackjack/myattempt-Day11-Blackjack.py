from replit import clear
from random import choice
def wanna_exit():
  if input("Do you wish to exit? ").lower()=="yes":
    return False
  else:
    return True
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
to_play=True
while to_play:
  clear()
  usercards=[choice(cards),choice(cards)]
  userscore=sum(usercards)
  if 11 in usercards and userscore>21:
    usercards[usercards.index(11)]=1
    userscore=sum(usercards)
  compcards=[choice(cards),choice(cards)]
  compscore=sum(compcards)
  if 11 in compcards and compscore>21:
    compcards[compcards.index(11)]=1
    compscore=sum(compcards)
  print(f"Your cards: {usercards}. Your current score: {userscore}")
  print(f"Computer's first card: {compcards[0]}")
  if userscore>21 and compscore>21:
    print(f"It's a tie. Both user's and computer's score exceeded 21.")
    print(f"Computer's cards: {compcards}. Computer's score: {compscore}")
    to_play=wanna_exit()
  elif userscore>21:
    print(f"You Lose. Your score exceeds 21.")
    print(f"Computer's cards: {compcards}. Computer's score: {compscore}")
    to_play=wanna_exit()
  elif compscore>21:
    print(f"You Win. Computer's score exceeds 21.")
    print(f"Computer's cards: {compcards}. Computer's score: {compscore}")
    to_play=wanna_exit()
  elif compscore==21:
    print(f"You Lose. Computer got a Blackjack.")
    print(f"Computer's cards: {compcards}. Computer's score: {compscore}")
    to_play=wanna_exit()
  elif userscore==21:
    print(f"You Win. You got a Blackjack")
    print(f"Computer's cards: {compcards}. Computer's score: {compscore}")
    to_play=wanna_exit()
  else:
    to_draw=True
    while to_draw:
      if userscore>=21:
        to_draw=False
      else:
        draw=input("Wanna draw a card? ").lower()
        if draw=="yes":
          usercards.append(choice(cards))
          userscore=sum(usercards)
          if 11 in usercards and (userscore>21):
            usercards[usercards.index(11)]=1
            userscore=sum(usercards)
          print(f"Your cards: {usercards}. Your current score: {userscore}")
        else:
          to_draw=False
    if userscore>21:
      print(f"You Lose. Your score exceeded 21")
      print(f"Computer's cards: {compcards}. Computer's score: {compscore}")
      to_play=wanna_exit()
    else:
      while compscore<17:
        compcards.append(choice(cards))
        compscore=sum(compcards)
        if 11 in compcards and compscore>21:
          compcards[compcards.index(11)]=1
          compscore=sum(compcards)
      if compscore>21:
        print(f"You Win. Computer's score exceeds 21.")
        print(f"Computer's cards: {compcards}. Computer's score: {compscore}")
        to_play=wanna_exit()
      elif userscore==compscore:
        print(f"It's a tie.")
        print(f"Computer's cards: {compcards}. Computer's score: {compscore}")
        to_play=wanna_exit()
      elif userscore>compscore:
        print(f"You win!")
        print(f"Computer's cards: {compcards}. Computer's score: {compscore}")
        to_play=wanna_exit()
      elif compscore>userscore:
        print(f"You Lose")
        print(f"Computer's cards: {compcards}. Computer's score: {compscore}")
        to_play=wanna_exit()
        
        
      
    
    
