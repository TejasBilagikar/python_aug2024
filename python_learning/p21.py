#Program to print a Hollow Square of N lines

num_lines = int(input('Enter number of lines to draw the square: '))

print('* ' * num_lines)
for i in range(num_lines - 2):
    print('* ' + ' ' * (num_lines * 2 - 4) + '* ' )
print('* ' * num_lines)


'''
for i in range(1, num_lines + 1):
    for j in range(1, num_lines + 1):
        if j == 1 or j == num_lines or i == j or j == num_lines - i + 1:
            print('* ', end='')
        else:
            print(' ', end='')
    print()

'''