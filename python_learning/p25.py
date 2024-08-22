# Assume 1 and 2 are 1st 2 terms of the series and print the 1st N term of Fibo series (HemaChandra numbers).

n_terms = int(input('Enter the number of terms of Fibonacci sequence: '))
first_term = 1
sec_term = 2
temp_term = 0
if n_terms < 1:
    print('Invalid input: Enter a positive number')
else:
    print(f'Fibonacci sequence for {n_terms} terms is: ')
    for i in range(n_terms):
        print(first_term)
        temp_term = sec_term
        sec_term = first_term + sec_term
        first_term = temp_term