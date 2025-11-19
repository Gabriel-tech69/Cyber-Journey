#!/usr/bin/env python3
max_attempts = 3
attempts = 0
locked = False
while attempts < max_attempts and not locked:
    password = input('Enter your password: ')
    if password == 'password123':
        print("Access Granted")
        break
    else: 
        attempts = attempts + 1
        if attempts == max_attempts:
            locked = True
            print("ACCOUNT LOCKED - Too many failed attempts")
        else:
            print(f"wrong password {max_attempts - attempts} remaining")
