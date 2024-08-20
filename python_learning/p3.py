'''
Accept a number as input, say X and define logic to get output say Y. The input can only be 0 or 1 and the otput must be 1 if input is 0 and viceversa.
'''

X = int(input('Enter the input number(0 or 1 only): '))

if X == 0 or X == 1:
    Y = 1 - X
    print(f'The output is {Y}')
else:
    print('Invalid input')
