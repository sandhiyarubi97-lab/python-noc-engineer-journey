import csv

csv_path = r'C:\Users\Santhiya R\python-noc-journey\Day07 interfaces.csv\parse_interfaces.py'

data = [
    ["Interface", "IP-Address", "Status", "Protocol"],
    ["GigabitEthernet1", "10.10.20.48", "up", "up"],
    ["GigabitEthernet2", "unassigned", "down", "down"],
    ["GigabitEthernet3", "unassigned", "administratively down", "down"],
    ["Loopback0", "1.1.1.1", "up", "up"],
    ["Loopback100", "100.100.100.100", "down", "down"]
]

with open(csv_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print(f"CSV created at: {csv_path}")