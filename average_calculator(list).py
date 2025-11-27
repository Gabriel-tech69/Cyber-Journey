#!/usr/bin/env python3
def average():
    numlist = list()
    while True:
        inp = input("Enter number: ")
       
        if inp == 'done':
            break
        num = float(inp)
        numlist.append(num)
    average = sum(numlist) / len(numlist)
    print("Average =", average)
    print(f"The average of numbers is {average}")
def main():
    print("=== YAHIKO'S AVERAGE CALCULATOR ===\n")
    print("Enter '1' to input value")
    print("Enter '2' to quit\n")
    print("NOTE: Enter 'done' after inputing the preffered numbers\n")
    
    action = input("Enter what action you wish to perform: ")
    try:
        if action == '1':
            average()
        elif action == '2':
            print("...........................\n")
            print("Goodbye!")
    except:
        print("Invalid Input")
main()
