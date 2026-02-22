#!/usr/bin/env python3

from netmiko import ConnectHandler

source_ip = "172.16.1.2"
loopback1 = "192.168.1.1"
loopback2 = "192.168.1.65"
our_loopback3 = "192.168.1.129"
oth_loopback3 = "192.168.2.129"

router_info = {
    "device_type": "cisco_ios",
    "host": source_ip,
    "username": "admin",
    "password": "cisco"
}

net_connect = ConnectHandler(**router_info)
our_lo1_lo3 = net_connect.send_command(f"traceroute {our_loopback3} source {loopback1}")
our_lo2_lo3 = net_connect.send_command(f"traceroute {our_loopback3} source {loopback2}")
oth_lo1_lo3 = net_connect.send_command(f"traceroute {oth_loopback3} source {loopback1}")
oth_lo2_lo3 = net_connect.send_command(f"traceroute {oth_loopback3} source {loopback2}")
print(f"--- Lo1 ({loopback1}) --> Lo3 ({our_loopback3}) ---\n{our_lo1_lo3}\n")
print(f"--- Lo2 ({loopback2}) --> Lo3 ({our_loopback3}) ---\n{our_lo2_lo3}\n")
print(f"--- Lo1 ({loopback1}) --> Lo3 ({oth_loopback3}) ---\n{oth_lo1_lo3}\n")
print(f"--- Lo2 ({loopback2}) --> Lo3 ({oth_loopback3}) ---\n{oth_lo2_lo3}\n")
net_connect.disconnect()
