# Check if a number is Prime.

input_num = int(input('Enter a number to check if it is a Prime number: '))
if input_num > 1:
  for i in range(2, input_num):
    if input_num % i == 0:
      print(f'{input_num} is not a Prime number')
      break
  else:
    print(f'{input_num} is a Prime number.')

else:
  print('Invalid input.')
