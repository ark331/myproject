# Stone paper scissors game
print("Hello main.py") 
import random 

def choice(p1, p2) :
  list = ['Rock', 'Paper', 'Scissors']
  if p1 == 'Rock' and p2 == 'Rock' or p1=='Scissors' and p2=='Scissors' or p1=='Paper' and p2=='Paper':
    return "Match Drawn"
  elif p1=='Rock' and p2=='Scissors' or p1=='Scissors' and p2=='Paper' or p1=='Paper' and p2=='Rock' :
    return " Player 1 Won the game!!! "
  else :
    return "Player 2 won the game!!! "

player1 = input("Enter your Choice (Rock, Paper, Scissor)") 
print("Computer selecting moves") 
print("Calculating probabilities ") 
player2 = random.choice(list) 
                
check(player1, player
