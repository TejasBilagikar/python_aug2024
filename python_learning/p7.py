#Code to check if a number is a Perfect square.

print('Code to check if a number is a Perfect square.')
my_num = int(input('Enter a number: '))
sqrt_num = my_num ** 0.5
if sqrt_num == int(my_num ** 0.5):
  print(f'{my_num} is a perfect square.')