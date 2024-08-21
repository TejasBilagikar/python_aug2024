#Program to check if an alphabet is uppercase.

input_alpha = input('Enter the input alphabet: ')
if len(input_alpha) > 1:
  print('Enter only one character'
  )
elif input_alpha.isupper():
  print("Alphabet is in uppercase.")