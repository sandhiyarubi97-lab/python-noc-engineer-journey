from netmiko import ConnectHandler
import time
from datetime import datetime

device = {
    'device_type': 'cisco_ios',
    'ip': 'sandbox-iosxe-latest-1.cisco.com',
    'port': 8181,
    'username': 'developer',
    'password': 'C1sco12345',
    'secret': 'C1sco12345'
}

print("Starting 24x7 monitoring... Press Ctrl+C to stop")

while True:
    try:
        print(f"\n[{datetime.now()}] Connecting to device...")
        conn = ConnectHandler(**device)
        conn.enable()  # Enter enable mode

        output = conn.send_command('show version | include Version|uptime')
        print("NOC Output:")
        print(output)

        conn.disconnect()
        print("Waiting 5 mins for next check...")
        time.sleep(300)  # 300 sec = 5 mins

    except Exception as e:
        print(f"NOC Alert: Connection failed - {e}")
        time.sleep(60)  # Wait 1 min then retry