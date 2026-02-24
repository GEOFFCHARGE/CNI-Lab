#!/usr/bin/env python3

from netmiko import ConnectHandler

source_ip = "172.16.1.2"
loopback1 = "192.168.1.1"
loopback2 = "192.168.1.65"
oth_loopback3 = "192.168.2.129"

clockwise = "172.16.1.9"
countercw = "100.100.4.2"

router_info = {
    "device_type": "cisco_ios",
    "host": source_ip,
    "username": "admin",
    "password": "cisco"
}

net_connect = ConnectHandler(**router_info)
command = [
    "no access-list 101",
    "no access-list 102",
    "no route-map SPLIT_TRAFFIC",
    "no ip local policy route-map SPLIT_TRAFFIC",
    f"access-list 101 permit ip host {loopback1} host {oth_loopback3}",
    f"access-list 102 permit ip host {loopback2} host {oth_loopback3}",
    "route-map SPLIT_TRAFFIC permit 10",
    " match ip address 101",
    f" set ip next-hop {clockwise}",
    "exit",
    "route-map SPLIT_TRAFFIC permit 20",
    " match ip address 102",
    f" set ip next-hop {countercw}",
    "exit",
    "ip local policy route-map SPLIT_TRAFFIC"
]
net_connect.send_config_set(command)
oth_lo1_lo3 = net_connect.send_command(f"traceroute {oth_loopback3} source {loopback1}")
oth_lo2_lo3 = net_connect.send_command(f"traceroute {oth_loopback3} source {loopback2}")
print(f"--- Lo1 ({loopback1}) --> Lo3 ({oth_loopback3}) ---\n{oth_lo1_lo3}\n")
print(f"--- Lo2 ({loopback2}) --> Lo3 ({oth_loopback3}) ---\n{oth_lo2_lo3}\n")
net_connect.disconnect()
