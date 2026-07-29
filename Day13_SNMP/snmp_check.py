import csv
from datetime import datetime
import os
import random
import time

DEVICES = [
    {"name": "R1-Core", "ip": "192.168.1.1"},
    {"name": "SW1-Access", "ip": "192.168.1.2"},
    {"name": "FW1-Edge", "ip": "192.168.1.3"},
]


def get_fake_snmp_data(device):
    # this is fake data
    cpu = random.randint(20, 95)
    mem = random.randint(30, 90)

    cpu_status = "CRITICAL" if cpu > 85 else "WARNING" if cpu > 70 else "OK"
    mem_status = "CRITICAL" if mem > 85 else "WARNING" if mem > 70 else "OK"

    return {
        "Device": device["name"],
        "IP": device["ip"],
        "CPU_%": cpu,
        "CPU_Status": cpu_status,
        "Memory_%": mem,
        "Memory_Status": mem_status,
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


def main():
    data = []
    for d in DEVICES:
        data.append(get_fake_snmp_data(d))

    # CSV save
    csv_file = "snmp_report_latest.csv"
    with open(csv_file, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print(f"SNMP Scan Complete. Report saved: {csv_file}")

    # copying to Dashboard
    dst = "../Day17_Dashboard/snmp_report_latest.csv"
    os.makedirs("../Day17_Dashboard", exist_ok=True)
    import shutil
    shutil.copy(csv_file, dst)
    print(f"Copied to Dashboard: {dst}")

if __name__ == "__main__":
    main()


CSV_PATH = "snmp_report_latest.csv"


def save_history():
    history_path = "snmp_history.csv"
    file_exists = os.path.exists(history_path)

    # read current report
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        devices = list(reader)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # append to history
    with open(history_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Timestamp', 'Device', 'CPU_%', 'Memory_%'])
        for d in devices:
            writer.writerow([timestamp, d['Device'], d['CPU_%'], d['Memory_%']])


save_history()

