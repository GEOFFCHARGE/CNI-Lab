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
    spec = net_connect.send_command("sh version")
    intf = net_connect.send_command("sh ip int br")
    rout = net_connect.send_command("sh ip rou")
    print(f"--- {ip} Hostname ---\n{name}\n")
    print(f"--- {ip} Specification ---\n{spec}\n")
    print(f"--- {ip} Interface ---\n{intf}\n")
    print(f"--- {ip} Routing Table ---\n{rout}\n")
    net_connect.disconnect()
