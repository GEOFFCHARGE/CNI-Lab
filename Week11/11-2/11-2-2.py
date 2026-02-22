#!/usr/bin/env python3

from netmiko import ConnectHandler

router_ip = []

print("Enter Router IP one by one (type 'OK' to finish):")

while True:
    ip = input("IP: ")
    if ip.upper() == "OK":
        break
    router_ip.append(ip)

for router in router_ip:
    router_info = {
        "device_type": "cisco_ios",
        "host": router,
        "username": "admin",
        "password": "cisco"
    }
    net_connect = ConnectHandler(**router_info)
    name = net_connect.send_command("sh run | include name")
    intf = net_connect.send_command("sh ip int br")
    traf = net_connect.send_command("sh int | include line protocol | input rate | output rate")
    print(f"--- {router} Hostname ---\n{name}\n")
    print(f"--- {router} Interface ---\n{intf}\n")
    print(f"--- {router} Traffic ---\n{traf}\n")
    net_connect.disconnect()
