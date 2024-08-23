# Program to Find Odd(Even) placed digits in a number.

input_num = int(input("Enter a number: "))
count = 0
temp_num = input_num
set1 = 0
set2 = 0

while temp_num != 0:
  digit = temp_num % 10
  temp_num = temp_num // 10
  if digit != 0:
    set1 = set1 * 10 + digit
    count += 1
  digit = temp_num % 10
  temp_num = temp_num // 10
  if digit != 0:
    set2 = set2 * 10 + digit
    count += 1

if count % 2 == 0:
  print(f'Even placed digits in {input_num} are: {set2}')

elif count % 2 != 0:
  print(f'Even placed digits in {input_num} are: {set1}')