#Program to print Math table for a number.

print('Program for Math table of a number.')
num = int(input('Enter a number: '))
print(f'Math table for {num}: ')
for i in range(1,21):
  print(f'{num:02d} x {i:02d} = {num * i:03d}')