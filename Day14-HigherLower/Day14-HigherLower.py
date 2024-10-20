import art, game_data, random, replit
#game_data available at: https://replit.com/@appbrewery/higher-lower-start#game_data.py
#art available at: https://replit.com/@appbrewery/higher-lower-start#art.py
def compare_followers(personA,personB):
  if personA["follower_count"]>personB["follower_count"]:
    return personA["name"]
  else:
    return personB["name"]
def select_celeb(already_selected):
  index=random.randint(0,len(game_data.data)-1)
  while True:
    if index in already_selected:
      index=random.randint(0,len(game_data.data)-1)
    else:
      global some_list
      some_list.append(index)
      return game_data.data[index]
def celeb_description(person):
  return (f"{person['name']}, a {person['description']}, from {person['country']}")
def game():
  print(art.logo)
  celebA=select_celeb(some_list)
  celebB=select_celeb(some_list)
  score=0
  to_continue=True
  while to_continue:
    print(f"\nA:", celeb_description(celebA))
    print(art.vs)
    print(f"B:", celeb_description(celebB))
    higher=compare_followers(celebA,celebB)
    choice=input("\nWho has higher followers? 'A' or 'B': ").lower()
    replit.clear()
    print(art.logo)
    if (choice=="a" and higher==celebA['name']) or (choice=="b" and higher==celebB['name']):      
      print(f"You guessed it right!")
      score+=1
      celebA=celebB
      celebB=select_celeb(some_list)
    else:      
      print(f"Wrong guess!")
      print(f"\nGAME OVER.")
      to_continue=False
    print(f"Your score: {score}")
some_list=[]
game()

