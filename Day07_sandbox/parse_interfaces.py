from netmiko import ConnectHandler
import csv
from datetime import datetime

cisco_router = {
    'device_type': 'cisco_ios',
    'host': 'sandbox-iosxe-latest-1.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'port': 22,
}
print("Connecting to router...")
try:
    net_connect = ConnectHandler(**cisco_router)        #net_coonect : base connection
    output = net_connect.send_command("show interface brief")
    net_connect.disconnect()

    print("----raw router output----")
    print(output)
    print("---parsing---")

    #parse the output
    lines = output.splitlines()
    interfaces = []

    for line in lines:
        #skip header lines and empty lines
        if 'Interface' in line or line.strip() == '':
            continue
        parts = line.split()
        if len(parts) >= 6:
            interface = {
                'interface': parts[0],
                'ip_address': parts[1],
                'status': parts[4],
                'protocol': parts[5]
            }
            interfaces.append(interface)
    #Save to csv
    csv_file = 'Day07/interfaces.csv'
    with open(csv_file, 'w', newline='')as f:
        writer = csv.DictWriter(f, fieldnames=['interface', 'ip_address', 'status', 'protocol'])
        writer.writeheader()
        writer.writerows(interfaces)
    print(f"saved {len(interfaces)} interfaces to {csv_file}")
    print(f"Done at {datetime.now}")
except Exception as e:
    print(f"failed: {e}")





