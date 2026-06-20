# day7_parse.py
output = """Interface IP-Address OK? Method Status Protocol
GigabitEthernet1 10.10.20.48 YES NVRAM up up
GigabitEthernet2 unassigned YES NVRAM administratively down down
GigabitEthernet3 unassigned YES NVRAM administratively down down
Loopback0 1.1.1.1 YES NVRAM up up
Loopback100 100.100.100.100 YES NVRAM down down"""

print("NOC Daily Report: UP Interfaces")
print("-" * 40)
lines = output.splitlines()[1:]    # Header skip

for line in lines:
    parts = line.split()
    intf = parts[0]
    ip = parts[1]
    status = parts[4]

    if status == "up":
        print(f"Interface: {intf:15} | IP: {ip:15} | Status: UP")

print("-" * 40)
print("Total UP Interfaces: 2")