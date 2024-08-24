# Print Prime numbers between M and N (M < N).

start_num = int(input('Enter the start number: '))
end_num = int(input('Enter the end number: '))

prime_list = []
if start_num < end_num and start_num > 1:
  for i in range(start_num, end_num):
    for j in range(2, i):
      if i % j == 0:
        break
    for j in range(2, i):
      if i % j == 0:
        break
      
elif start_num > end_num:
  print('Invalid input: The start number should be less than the end number.')
