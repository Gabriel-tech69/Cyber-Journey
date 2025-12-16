#!/usr/bin/env python3
port = {"22": "SSH", "80": "HTTP", "443": "HTTPS", "3389": "RDP"}
while True:
    print("=====PORT TO SERVICE MAPPER=====")
    print("Enter the action you wish to perform")
    print("1. Show all port-service pair")
    print("2. Look up what service runs on a port")
    print("3. Add or remove port")
    print("4. Check if port exits in list")
    print("5. Quit")
    act = input("Enter what action you wish to perform: ")
    if act == "1":
        print(port)
    elif act == "2":
        inp = input("Enter the port number: ")
        inp = int(inp)
        if isinstance(inp, int):
            port[f"{inp}"]
            print(port[f"{inp}"])
        else:
            print("Enter port number as integer or Port & Service not available in list")
    elif act == "3":
        print("Enter 1 to Add port")
        print("Enter 2 to remove port")
        inp = input("Enter what action you wish to perform: ")
        if inp == '1':
            num = input("Enter the port number: ")
            ser = input("Enter the service: ")
            num = int(num)
            ser = str(ser)
            if isinstance(num, int) and isinstance(ser, str):
                port[f"{num}"] = f"{ser}"
                print("Port Added......")
            else:
                print("Enter valid input")
        elif inp == '2':
            num = input("Enter the port number: ")
            num = int(num)
            if f"{num}" in port:
                del port[f"{num}"]
                print("Port Removed......")
            else:
                print("Port/Service is not in the list")
    elif act == '4':
        inp = input("Enter port number: ")
        inp = int(inp)
        if f"{inp}" in port:
            print("Port is on the list")
        else:
            print("Port is not on the list")
    elif act == '5':
        break
    else:
        print("Enter a valid input")
