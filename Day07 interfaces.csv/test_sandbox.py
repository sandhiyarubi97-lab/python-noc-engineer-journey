from netmiko import ConnectHandler

creds_list = [
    {'username': 'developer', 'password': 'C1sco12345'},
    {'username': 'developer', 'password': 'C1sco123456'},
    {'username': 'admin', 'password': 'C1sco12345'},
]

for cred in creds_list:
    device = {
        'device_type': 'cisco_ios',
        'host': 'sandbox-iosxe-latest-1.cisco.com',
        'port': 22,
        **cred
    }
    try:
        print(f"Trying {cred['username']}/{cred['password']}...")
        net_connect = ConnectHandler(**device)
        output = net_connect.send_command("show version | i uptime")
        print("SUCCESS! Output:", output)
        net_connect.disconnect()
        break
    except Exception as e:
        print(f"Failed: {e}\n")