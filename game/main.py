import random
import os
no_of_games = 3
games_played = 0
choices = ['rock' , 'paper' , 'scissor']


  
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
  
    
  computer_choice = random.choice(choices)
  if computer_choice == 'scissor':
    print("Computer wins")
    games_played = games_played + 1
  else:
    print("You win")
    games_played = games_played + 1
            
return paper()

def scissor():
  computer_choice = random.choice(choices)
  if computer_choice == 'rock':
    print("Computer wins")
    games_played = games_played + 1
  else:
    print("You win")
    games_played = games_played + 1
    
return scissor()
  
  
    
  
  
