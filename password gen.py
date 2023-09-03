from random import choice

def count():
    n = input("How many passwords do you need? Enter a number: ")
    while n.isdigit() == False:
        print("You need to enter a number!")
        n = input("How many passwords do you need? Enter a number: ")
    return int(n)

def long():
    l = input("Enter password length: ")
    while l.isdigit() == False:
        print("You need to enter a number!")
        l = input("Enter password length: ")
    return int(l)

def is_number():
    isn = input('Do you need the numbers 0123456789 in your password? Write "yes" or "no": ')
    while isn.lower() not in ['yes', 'no']:
        print('You must enter "yes" or "no".')
        isn = input('Do you need the numbers 0123456789 in your password? Write "yes" or "no": ')
    return isn

def is_upper():
    isup = input('Do you need capital letters in the password? Write "yes" or "no": ')
    while isup.lower() not in ['yes', 'no']:
        print('You must enter "yes" or "no".')
        isup = input('Do you need capital letters in the password? Write "yes" or "no"')
    return isup

def is_lower():
    islw = input('Do you need lowercase letters in your password? Write "yes" or "no": ')
    while islw.lower() not in ['yes', 'no']:
        print('You must enter "yes" or "no".')
        islw = input('Do you need lowercase letters in your password? Write "yes" or "no": ')
    return islw
    
def is_symbol():
    issmb = input('Are characters required in the password? Write "yes" or "no": ')
    while issmb.lower() not in ['yes', 'no']:
        print('You must enter "yes" or "no".')
        issmb = input('Are characters required in the password? Write "yes" or "no": ')
    return issmb

def is_ambiguous():
    amb = input('Will there be ambiguous characters in the password "il1Lo0O"? Write "yes" or "no": ')
    while amb.lower() not in ['yes', 'no']:
        print('You must enter "yes" or "no".')
        amb = input('Will there be ambiguous characters in the password "il1Lo0O"? Write "yes" or "no": ')
    return amb

def gen_chars():
    chars = ''
    if isn == 'yes':
        chars += '0123456789'
    if isup == 'yes':
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if islw == 'yes':
        chars += 'abcdefghijklmnopqrstuvwxyz'
    if issmb == 'yes':
        chars += '!#$%&*+-=?@^_'
    if amb == 'no':
        for i in range(len(chars)):
            if chars[i] in 'il1Lo0O':
                del chars[i]
    return chars

def build_password():
    for i in range(n):
        password = []
        for i in range(l):
            password.append(choice(chars))
        print(''.join(password))
        

n = count()
l = long()
isn = is_number()            
isup = is_upper()
islw = is_lower()
issmb = is_symbol()
amb = is_ambiguous()
chars = gen_chars()
build_password()
