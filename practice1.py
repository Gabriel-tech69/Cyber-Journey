#!/usr/bin/env python3
try:
    while True:
        num = input('Enter a positive number (or "quit"): ')
        if num == 'quit':
            print('Process Quit')
            break
 
        num = int(num)
        if num < 0:
            print('Skipping negative number .... ')
            continue
        print(f"Processing: {num}")
except:
    print('Invalid input')
