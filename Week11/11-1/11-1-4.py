#!/usr/bin/env python3

from netmiko import ConnectHandler

router_ip = ["172.16.1.1", "172.16.1.2", "172.16.1.6"]

for i, ip in enumerate(router_ip, 1):
    router_info = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "admin",
        "password": "cisco"
    }
    net_connect = ConnectHandler(**router_info)
    name = f"{net_connect.find_prompt()[:-1]}s"
    pswd = f"cisco{i}"
    command = [f"hostname {name}", f"enable password {pswd}"]
    net_connect.send_config_set(command)
    print(f"--- {ip} Hostname and Password was change ---\nHostname: {name}\nPassword: {pswd}\n")
    net_connect.disconnect()
