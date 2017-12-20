# the daily practice

# 1. "is_even"

# 2. " string_length"
    # solution (1)



    # solution (2)

#test_string_length()


#3 "last_letter"

#4 "find_number"

#5 "biggest_guy"

#  solution (1)

#  solution(2)

#sum of list

# square a list, using append

# split , index, and find

# use append use loop


#use replace() for string
'''
# marker = 'is'
# replacement = 'was'
#line = 'that is nice, that is nice'
# new_line = line.replce(marker, replacement,2)
#output should be: 'that was nice, that was nice'

'''




#project(3)
'''
create a tic tac toc game
'''


#project(2):
#create a password generater that generates a password contains 8 characters,
#include 1 upper case and 3 numbers

'''
import string
import random

def password_generator():
    special = '@#$%&_'
    letter_1 = random.choice(special)
    letter_2 = random.choice(string.ascii_lowercase)
    letter_3 = random.choice(string.ascii_lowercase)
    letter_4 = random.choice(string.ascii_uppercase)
    letter_5 = random.choice(string.digits)
    letter_6 = random.choice(string.digits)
    letter_7 = random.choice(string.digits)
    letter_8 = random.choice(string.ascii_uppercase)
    password = letter_1+letter_2+letter_3+letter_4+letter_5+letter_6+letter_7+letter_8
    return password
for i in range(10):
    
    print(password_generator())
    
'''

#project (1):

#create password that contains 'numbers 0 to 9',letter'a to z',
#at least 1 special characters, at least 8 characters long,
#and at least one upper case letter
'''
password = input('password:')


def password_check(password):
    upper_case = 0
    lower_case = 0
    number = 0
    symbol = 0

    for i in password:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
        elif i.isdigit():
            number += 1
        else:
            symbol += 1
    
    if len(password)>= 8:    
        if upper_case>0 and lower_case>0 and number>0 and symbol>0:
            return 'Looking good'
        elif upper_case==0:
            return 'password must contain at least 1 upper case letter'
        elif lower_case==0:
            return 'password must contain at least 1 lower case letter'
        elif number==0:
            return 'password must contain at least 1 number'
        elif symbol==0:
            return 'password must contain at least 1 special symbol'
    else:
        return 'password must be at least 8 characters'

print(password_check(password))
    
'''
