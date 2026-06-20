from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_ios',
    'host': 'ios-xe-mgmt-latest.cisco.com',
    'username': 'developer',
    'password': 'C1sco12345',
    'port': 22,
}

print("Connecting......")
try:
    net_connect = ConnectHandler(**cisco_router)
    output = net_connect.send_command("show ip int brief")
    print(output)
    net_connect.disconnect()
    print("\n SUCCESS -Day 7 Done")
except Exception as e:
    print(f"Failed: {e}")
