#!/usr/bin/env python3

from netmiko import ConnectHandler

router_ip = ["172.16.1.1", "172.16.1.2", "172.16.1.6"]

for ip in router_ip:
    router_info = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "admin",
        "password": "cisco"
    }
    net_connect = ConnectHandler(**router_info)
    name = net_connect.find_prompt()[:-1]
    intf = net_connect.send_command("sh ip int br")
    traf = net_connect.send_command("sh int | include line protocol | input rate | output rate")
    print(f"--- {ip} Hostname ---\n{name}\n")
    print(f"--- {ip} Interface ---\n{intf}\n")
    print(f"--- {ip} Traffic ---\n{traf}\n")
    net_connect.disconnect()
