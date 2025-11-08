#!/usr/bin/env python3 
device1_name = "laptop"
device1_ip = "172.20.10.4"
device1_type = "end_device"
device1_status = True # True = Online, False = Offline
device2_name = "ipad"
device2_ip = "172.20.10.3"
device_type ="end_device"
device2_status = False
device2_type = "end device"
device3_name = "router"
device3_ip = "172.20.10.1"
device3_name = "mtn 5g"
device3_type = "router"
device3_status = True
def display_device_info(name, type, ip, status):
     if status:
         status_text = "Online"
     else:
         status_text = "Offline"
     title = name + " is an " + type + " with ip address " + ip + " and is currently " + status_text
     return title


device1 = display_device_info(device1_name, device1_type, device1_ip, device1_status)
device2 = display_device_info(device2_name, device2_type, device2_ip, device2_status)
device3 = display_device_info(device3_name, device3_type, device3_ip, device3_status)
print(device1)
print(device2)
print(device3)
