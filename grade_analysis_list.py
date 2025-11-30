#!/usr/bin/env python3
def grade_analysis():
    numlist = []
    highest = None
    smallest = None
    
    while True:
        inp = input("Enter a grade: ")
        
        if inp == 'done':
            break
        num = float(inp)
        if 0 <= num <= 100:
            numlist.append(num)
            
            
            
        
        else:
            print("Enter a positive value or a range of values between 1-100")
    for numl in numlist:
       
        if highest is None or numl > highest:
            highest = numl
        elif smallest is None or numl < smallest:
            smallest = numl
    sum(numlist)
    len(numlist)
    average = sum(numlist) / len(numlist)
    print(f"Average: {average}")
    print(f"Highest grade: {highest}")
    print(f"Lowest grade: {smallest}")
grade_analysis()
