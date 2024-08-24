# Find Nth Fibo term (assume 1 and 2 as 1st 2 terms)


input_num = int(input('Enter the number to find the Nth number in Fibonacci sequence: '))
num1, num2 = 1, 2

if input_num == 1:
  print('The 1st number in Fibonacci sequence is: 1')
elif input_num > 1:
  for i in range(2, input_num + 1):
    num1, num2 = num2, num1 + num2

print(f'The {input_num}th number in Fibonacci sequence is: {num1}') 
