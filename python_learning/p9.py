#Program to print Math table for a number.

print('Code for Math table of a number.')
num = int(input('Enter a number: '))
print(f'Math table for {num}: ')
for i in range(1,11):
  print(f'{num} x {i:2d} = {num * i}')