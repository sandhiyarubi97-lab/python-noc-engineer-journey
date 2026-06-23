from netmiko import ConnectHandler
import textfsm
import datetime
import os

device = {
    'device_type': 'cisco_ios',
    'host': 'sandbox-iosxe-latest-1.cisco.com',
    'username': 'developer',
    'password': 'C1sco12345',
}

try:
    print("Connecting to device...")
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_command("show version")
        print("Device Connected - Parsing Live Data")

except Exception as e:
    print(f"NOC Alert: Connection failed - {e}")
    print("Using mock data for demo...")
    output = """R1 uptime is 5 weeks, 2 days
Cisco IOS Software, Version 15.2(4)M1, RELEASE SOFTWARE (fc1)"""

with open('templates/cisco_ios_show_version.textfsm') as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(output)

print("\nMock Structured Data:")
for row in result:
    print(f"Hostname: {row[0]}, IOS: {row[1].strip(',')}, Uptime: {row[2]}")

print("\n--------------------------------------------------")
print("Day 9 Complete: Backup + Parsing Done")