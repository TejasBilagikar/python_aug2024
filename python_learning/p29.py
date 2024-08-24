# Find sum of the series: n + n(2) + n(3) + ..... m terms.

print('Enter two numbers to find the sum of the series n + n(2) + n(3) + ..... m terms: ')
input_num = int(input('Enter the number: '))
end_num = int(input('Enter the end number: '))
total = 0

for i in range(1, end_num + 1):
  total = total + input_num * i

print(f'The sum is: {total}')
