#!/usr/bin/env python3
attempts = 3
while attempts > 0:
    password = input('Enter your password: ')
    if password == 'password123':
        print('Access granted')
        break
    else:
        attempts = attempts - 1 
        print(f'Wrong!, {attempts} attempts left')
if attempts == 0:
    print('Account locked')
