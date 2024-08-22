#Program to print a Hollow Square of N lines.

num_lines = int(input('Enter number of lines to draw the square: '))

print('* ' * num_lines)
for i in range(num_lines - 2):
    print('* ' + ' ' * (num_lines * 2 - 4) + '* ' )
print('* ' * num_lines)
