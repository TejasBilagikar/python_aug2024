'''
Accept average score from the student of his exam and print his result as follows:

0 to 49 is Fail
50 to 74 is second Clas
75 to 90 is first Class
91 to 100 is Distinction
Also check for invalid scores
'''

student_score = int(input('Enter average score: '))
if student_score < 0 or student_score > 100:
    print('Invalid score.')
elif student_score <= 49:
    print('Result: Fail')
elif student_score <= 74:
    print('Result: Second Class')
elif student_score <= 90:
    print('Result: First Class')
elif student_score <= 100:
    print('Result: Distinction')
