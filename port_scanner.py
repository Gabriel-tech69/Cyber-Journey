#!/usr/bin/env python3
common_ports = [21, 22, 23, 25, 53, 80, 443, 3389]
open_ports = [22, 80, 443]
for port in common_ports:
    if port in open_ports:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: Closed")
