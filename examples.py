# 10 Key Python Concepts

# 0. Comments always start with a #

# 1. We can assign Values to Variables ###############################

bananas = 10
apples = 15

# 2. We can write output #############################################

print('You have',bananas,'bananas')
print('This line will not end...', end='')
print('See?')
print('We can separate items', apples, bananas,'with a space')
print('Or maybe we don\'t want that', apples, bananas, sep='!')

# 3. We can read input and turn a str into an int ####################

oranges = input('How many oranges? ')
# oranges is a str() object, but we want an int()
oranges = int(oranges)
print('So, you have',oranges,'oranges.')

# 4. We can use if to make decisions #################################

if oranges < 0:
  print('You can\'t have negative oranges!')
if oranges == 1:
  print('You have an orange.');
elif oranges < 5:
  print('You have a few oranges.')
else:
  print('You have several oranges.')

# 5. We can iterate over a range #####################################

for pear in range(1,11):
  print('pear',pear)

# 6. We can loop while a condition is True ###########################

while True:
  print('orange',oranges)
  oranges = oranges - 1
  # you can leave a while loop with break
  if oranges <= 3:
      break;

# 7. We can create a list of items with list or [] ###################

mylist = ['apple', 'cherry', 'orange']
print(mylist)

for fruit in mylist:
  fruit += ' is delicious'
  print(fruit)

# Access index 0 (or first element of the list)
print(mylist[0])
# Access index 1 (or second element of the list)
print(mylist[1])
# Access index 2 (or third element of the list)
print(mylist[2])

# 8. We can use dictionaries with dict() or {} #######################

sportscars = {
  'ford': 'mustang',
  'chevy': 'camaro',
  'pontiac': 'trans am',
  'porsche': '911'
}

fordcar = sportscars['ford']
print(fordcar)

sportscars['chevy'] = 'corvette'
print(sportscars['chevy'])

for x, y in sportscars.items():
  print(x, y)

# 9. We can include libraries ########################################

from math import *

angleInDegrees = 45
angleInRadians = angleInDegrees * pi / 180.0

print('sin(', angleInDegrees, ') = ', sin(angleInRadians), sep='')

# 10. We can write functions #########################################

def fib(n):
  if n <= 0:
    return 0
  if n == 1:
    return 1
  return fib(n-1) + fib(n-2)

def testfib():
  for i in range(10):
    if i > 0:
      print(', ', end='')
    print(fib(i), end='')
  print()

testfib()
