#!/usr/bin/env python3
def smart_login():
    failed_count = 0
    success_count = 0
    total_attempts = 0
    while True:
        total_attempts <= 5
        failed_count <= 3
        attempt = input("Enter 'success' or 'fail' or 'done to finish':" )
        if attempt == 'success':
            success_count += 1
            print("Access granted")
        elif attempt == 'fail':
            failed_count += 1
            print("Access denied")
        elif attempt == 'done':
            print("Goodbye!")
            break
        else:
            print("Enter a valid input")
    print(f"\nFinal: {success_count} successful, {failed_count} failed logins")
    if total_attempts >= 5:
        print("Account locked")
    elif failed_count >= 3:
        print("Account locked")
def main():
    print("=== SMART LOGIN SYSTEM ===\n")
    smart_login()
main()
