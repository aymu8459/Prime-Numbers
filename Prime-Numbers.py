number = int(input('Enter a number: '))
if number == 2 or number == 3:
  print('number is a prime number')
elif number % 2 == 0 or number % 3 == 0 or number == 1 or number < 0:
  print('not a prime number')
else:
  print('number is a prime number')