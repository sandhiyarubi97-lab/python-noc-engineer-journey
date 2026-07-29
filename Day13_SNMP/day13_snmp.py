import csv
import random
from datetime import datetime

results = []


def get_status(value, critical=80, warning=60):
    if value >= critical:
        return "CRITICAL"
    elif value >= warning:
        return "WARNING"
    return "OK"


def check_snmp(name, ip, community):
    # Mock SNMP data - real device
    cpu = random.randint(5, 95)
    memory = random.randint(10, 90)

    cpu_status = get_status(cpu)
    mem_status = get_status(memory)

    print(f"{name:20} CPU: {cpu:3}% {cpu_status:8} MEM: {memory:3}% {mem_status:8}")

    results.append({
        'name': name,
        'ip': ip,
        'cpu': cpu,
        'cpu_status': cpu_status,
        'memory': memory,
        'mem_status': mem_status,
        'timestamp': datetime.now().strftime('%H:%M:%S')
    })


def save_csv_report():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    filename = f'snmp_report_{timestamp}.csv'

    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Device', 'IP', 'CPU_%', 'CPU_Status', 'Memory_%', 'Memory_Status', 'Timestamp'])
        for r in results:
            writer.writerow([
                r['name'],
                r['ip'],
                r['cpu'],
                r['cpu_status'],
                r['memory'],
                r['mem_status'],
                r['timestamp']
            ])

    print(f"\nCSV Report saved: {filename}")
    return filename


if __name__ == "__main__":
    print(f"Day 13: SNMP CPU+Memory Check at {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 75)

    # Device list -  devices
    devices = [
        {"name": "demo.snmplabs.com", "ip": "104.236.166.95", "community": "public"},
        {"name": "R1-Core", "ip": "192.168.1.1", "community": "public"},
        {"name": "R2-DMZ", "ip": "192.168.2.1", "community": "public"},
        {"name": "R3-WAN", "ip": "192.168.3.1", "community": "public"}
    ]

    start_time = datetime.now()

    for device in devices:
        check_snmp(device['name'], device['ip'], device['community'])

    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()

    print("-" * 75)
    print(f"Scanned {len(devices)} devices in {duration:.2f}s")

    # Critical count
    cpu_critical = sum(1 for r in results if r['cpu_status'] == 'CRITICAL')
    mem_critical = sum(1 for r in results if r['mem_status'] == 'CRITICAL')

    if cpu_critical > 0 or mem_critical > 0:
        print(f"ALERT: {cpu_critical} CPU CRITICAL, {mem_critical} MEM CRITICAL")
    else:
        print(" All devices healthy")

    save_csv_report()
