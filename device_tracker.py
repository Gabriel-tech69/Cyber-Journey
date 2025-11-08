#!/usr/bin/env python3
print("=== Network Device Status ===")
device1_name = input("Enter device 1 name: ")
device1_ip = input("Enter device 1 ip: ")
device1_status = input("Is device 1 online? (yes/no): ")
device2_name = input("Enter device 2 name: ")
device2_ip = input("Enter device 2 ip: ")
device2_status = input("Is device 2 online? (yes/no): ")
print("\n" + "="*40)
print("NETWORK DEVICE REPORT")
print("="*40)
if device1_status.lower() == "yes":
    print(f"✅ {device1_name} with ip  {device1_ip} is  ONLINE")
else:
    print(f"❌ {device1_name} with ip {device1_ip} is OFFLINE")
if device2_status.lower() == "yes":
    print(f"✅ {device2_name} with ip {device2_ip} is ONLINE")
else:
    print(f"❌ {device2_name} with ip {device2_ip} is OFFLINE")
print("\nReport generated successfully")
