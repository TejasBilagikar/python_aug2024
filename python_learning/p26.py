# Find the Nth Prime number.

input_num = int(input("Enter a number to find the Nth Prime number: "))

for i in range(1, input_num+1):
    for j in range(2, input_num ** 2):
      for k in range(2, input_num ** 2):
        if k > j or j % k == 0:
          print(f'{j} is not a Prime number')
          print(f'{j}/{k}')
          continue
      else:
        print(f'{j} is a Prime number.')
        print(j)
        #continue
print(f'The {i}th Prime number is: {j}')














'''
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
'''