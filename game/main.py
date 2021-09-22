import random
import os
no_of_games = 3
games_played = 0

while games_played < no_of games:
  no_of_games= input("How many games do you want to play?: ")

  
  while no_of_games != int:
    no_of_games= input("How many games do you want to play? Please put only integers: ")
  if no_of_games == int:
    no_of_games = no_of_games
    break
  
  
  def rock():
    if user.choice == "rock":
      choices = ['rock' , 'paper' , 'scissor']
      computer_choice = random.choice(choices)
    if computer_choice == 'paper':
        print("Computer wins")
        games_played = games_played + 1
     else:
      print("You win")
      games_played = games_played + 1
  return rock()
  def paper():
    if user.choice == 'paper':
      choices = ['rock' , 'paper' , 'scissor']
      computer_choice = random.choice(choices)
    if computer_choice == 'scissor':
      print("Computer wins")
      games_played = games_played + 1
    else:
      print("You win")
      games_played = games_played + 1
            
   return paper()
            
  
    
  
  
