# Stone paper scissors game
print("Hello main.py") 
def choice(p1, p2) :
  if p1 == 'Rock' and p2 == 'Rock' or p1=='Scissors' and p2=='Scissors' or p1=='Paper' and p2=='Paper':
    return "Match Drawn"
  elif p1=='Rock' and p2=='Scissors' or p1=='Scissors' and p2=='Paper' or p1=='Paper' and p2=='Rock' :
    return " Player 1 Won the game!!! "
  else :
    return "Player 2 won the game!!! "
c
