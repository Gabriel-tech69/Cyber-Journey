#!/usr/bin/env python3
threat = {"SQLi": 9, "XSS": 7, "RCE": 10, "DDOS": 6, "Brute force": 5}
def high_severity():
   
    severity = None
    for key, value in threat.items():
        if severity is None  or value > severity:
            severity = value
            skey = key
           
    print(f"The threat with the highest severity is {skey} with threat level at {severity}")
def edit_threat():
    inp = input("Enter threat name you wish to enter: ")
    sev = input("Enter the threat level: ")
    try:
        severity = int(sev)
        if 0 <= severity <= 10:
            
            threat[inp] = severity
            print("Threat Added")
        else:
            print("Enter severity level range 1-10")
    except:
        print("Enter a valid input")
def average_threat():
    total = sum(threat.values())
    length = len(threat.values())
    average = total / length
    print(f"The average threat severity is {average} for {length} threats.")
def critical_threat():
    for key, values in threat.items():
        if values >= 8:
            print("\n Threats with severity >= 8 are;")
            print(f"{key}: {values}")
def update_severity():
    inp = input("Enter threat name you wish to update severity: ")
    try:
        inp = inp.upper()
    except:
        print("Enter a valid input (not digits)")
    if inp in threat:
        for key, values in threat.items():
            if key == inp:
                ser = input("Enter the severity level of the threat: ")
                try:
                    ser = int(ser)
                    if 0 <= ser <= 10:
                        
                        threat[inp] = ser
                        print("Severity updated")
                except:
                    print("Enter a valid input (digit) between 0-10")
def remove_threat():
    inp = input("Enter threat name you wish to remove: ")
    try:
        inp = inp.upper()
    except:
        print("Enter a valid input (not digits)")
    if inp in threat:
        del threat[inp]
while True:
    print("\n ===== THREAT SEVERITY LEVEL =====")
    print("1. Display all threats with their severity levels")
    print("2. Add a new threat")
    print("3. Show Highest severity threat")
    print("4. Show Average severity")
    print("5. List all critical threats")
    print("6. Update severity of an existing threat")
    print("7. Remove a threat that has been mitigated")
    print("8. Quit")
    act = input("\nEnter what action you wish to perform: ")
    if act == "1":
        print(threat)
    elif act == "2":
        edit_threat()
    elif act == "3":
        high_severity()
        
    elif act == "4":
        average_threat()
    elif act == "5":
        critical_threat()
    elif act == "6":
        update_severity()
    elif act == "7":
        remove_threat()
    elif act == "8":
        print("\n Quitting process........")
        break
    else:
        print("Enter a valid input")
