#!/usr/bin/env python3
users = {"alice": "pass123", "bob": "secret456", "charlie": "qwerty789", "vic": "okay123", "pasque": "word342"}
while True:
    print("1. Add user")
    print("2. Remove user")
    print("3. Check if user exist")
    print("4. Change Password")
    print("5. List all users")
    print("6. Quit")
     
    choice = input('Enter your Choice: ')
    if choice == '1':
        add_user = input("Enter user you wish to add: ")
        add_pass = input("Enter password you wish to add: ")
        users[add_user] = add_pass
    elif choice == '2':
        user = input("Enter user you wish to remove: ")
        if user in users:
            del users[user]
            print(f"{user} removed from database")
        else:
            print(f"{user} not found in database")
    elif choice == '3':
        user = input("Enter user you wish to check: ")
        if user in users:
            print("User is in the database")
        else:
            print("user not in the database")
    elif choice == '4':
        user = input("Enter user you wish to change password: ")
        if user in users:
            user_pass = input("Enter password: ")
            users[user] = user_pass
        else:
            print("User not in the database")
    elif choice == '5':
        print(users)
    elif choice == '6':
        print("Goodbye........")
        break
    else:
        print("Enter a valid choice")
