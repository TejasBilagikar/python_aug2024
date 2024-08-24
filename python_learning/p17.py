# Program to Find Odd(Even) placed digits in a number.

input_num = int(input("Enter a number: "))
count = 0
temp_num = input_num
num_set1 = 0
num_set2 = 0

while temp_num != 0:
  digit = temp_num % 10
  temp_num = temp_num // 10
  if digit != 0:
    num_set1 = num_set1 * 10 + digit
    count += 1
  digit = temp_num % 10
  temp_num = temp_num // 10
  if digit != 0:
    num_set2 = num_set2 * 10 + digit
    count += 1

if count % 2 == 0:
  print(f'Even placed digits in {input_num} are: {num_set1}')       #for odd set2

elif count % 2 != 0:
  print(f'Even placed digits in {input_num} are: {num_set2}')       #for odd set1