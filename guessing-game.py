from random import *

def getchoice(prompt):
  choice = 0
  while choice <= 0:
    choice = int(input(prompt))
    if choice <= 0:
      print('Please enter a number between 1 and 10')
  return choice

while True:
  yesno = input('Would you like to play a guessing game? (y/n) ')
  if yesno == 'n':
    break
  if yesno != 'y':
    print('Sorry, please type y or n')
    continue
  answer = randint(1, 10)
  guess = 0
  while guess != answer:
    guess = getchoice('Guess a number between 1 and 10> ')
    if guess != answer:
      print('Sorry, that is not my number')
  print('Yay! you got it!')

print('Thanks for playing!')
