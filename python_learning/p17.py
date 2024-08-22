# Program to Find Odd(Even) placed digits in a number.

input_number=int(input('Enter a Number :'))
num=str(input_number)
odd_placed_num=''
for i in range(len(num)+1):
    if i % 2 == 0:
        odd_placed_num+=num[i]

print('Even placed digits in number is',odd_placed_num)