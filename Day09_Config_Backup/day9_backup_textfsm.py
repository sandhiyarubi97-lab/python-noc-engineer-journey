from netmiko import ConnectHandler
import textfsm
import os

device = {
    'device_type': 'cisco_ios',
    'host': 'sandbox-iosxe-latest-1.cisco.com',
    'username': 'developer',
    'password': 'C1sco12345',
    'port': 8181,
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
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, 'templates', 'cisco_ios_show_version.textfsm')

with open(template_path) as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(output)

print("\nMock Structured Data:")
for row in result:
    print(f"Hostname: {row[0]}, Uptime: {row[1]}, IOS: {row[2]}")
    print("Headers:", fsm.header)  # ['HOSTNAME', 'UPTIME', 'VERSION']
    print("Data:", result)  # [['R1', '5 weeks, 2 days', '15.2(4)M1']]

print("\n--------------------------------------------------")
print("Day 9 Complete: Backup + Parsing Done")