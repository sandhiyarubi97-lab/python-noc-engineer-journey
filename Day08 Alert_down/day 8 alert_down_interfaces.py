import csv
import os

csv_path = r'C:\Users\Santhiya R\python-noc-journey\Day07 interfaces.csv\parse_interfaces.py'

print("NOC Alert: DOWN Interface Check")
print("-" * 50)

if not os.path.exists(csv_path):
    print(f"ERROR: File not found at {csv_path}")
    exit()

with open(csv_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Skip header

    down_list = []
    for row in reader:
        # Fix: Empty row skip  + check if there is 4 column
        if not row or len(row) < 4:
            continue

        interface, ip, status, protocol = row
        if "down" in status.lower():
            down_list.append(f"{interface:20} | {ip:15} | {status}")

if down_list:
    print("ALERT: DOWN Interfaces Found!")
    for item in down_list:
        print(item)
    print(f"\nTotal: {len(down_list)} interfaces DOWN")
else:
    print("All interfaces UP. Green.")

print("-" * 50)