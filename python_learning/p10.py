#Program to check if an Alphabet is a vowel.

print('Code check if the alphabet is a Vowel or a Consonant.')
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
alpha = input('Enter an alphabet: ')
if alpha in vowels:
  print(f'{alpha} is a Vowel.')
elif alpha.isalpha():
  print(f'{alpha} is a Consonant.')
else:
  print('Invalid input.')