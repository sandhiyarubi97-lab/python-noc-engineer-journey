from pysnmp.hlapi import *
import threading
import time
import random
import csv
from datetime import datetime

OID_CPU_5SEC = '1.3.6.1.4.1.9.2.1.58.0'
OID_MEM_USED = '1.3.6.1.4.1.9.9.48.1.1.1.5.1'
OID_MEM_FREE = '1.3.6.1.4.1.9.9.48.1.1.1.6.1'

results = []

def snmp_get(host, oid, community='public'):
    try:
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(community, mpModel=0),
            UdpTransportTarget((host, 161), timeout=2, retries=1),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )
        errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
        if errorIndication or errorStatus:
            return None
        else:
            for varBind in varBinds:
                # Fix: Direct int convert,  no tuple
                return int(varBind[1])
    except:
        return None

def check_device_health(host):
    cpu = snmp_get(host, OID_CPU_5SEC)
    mem_used = snmp_get(host, OID_MEM_USED)
    mem_free = snmp_get(host, OID_MEM_FREE)

    # Mock fallback + type safety
    if cpu is None or not isinstance(cpu, int):
        cpu = random.randint(5, 95)
    if mem_used is None or not isinstance(mem_used, int):
        mem_used = random.randint(100, 900) * 1024 * 1024
    if mem_free is None or not isinstance(mem_free, int):
        mem_free = random.randint(100, 500) * 1024 * 1024

    mem_total = mem_used + mem_free
    # Fix: Zero division check + type safety
    mem_percent = int((mem_used / mem_total) * 100) if mem_total > 0 else 0

    cpu_alert = "CRITICAL" if cpu > 80 else "WARNING" if cpu > 60 else "OK"
    mem_alert = "CRITICAL" if mem_percent > 80 else "WARNING" if mem_percent > 60 else "OK"

    print(f"{host:<20} CPU: {cpu:>3}% {cpu_alert:<8} MEM: {mem_percent:>3}% {mem_alert}")
    results.append((host, cpu, cpu_alert, mem_percent, mem_alert))

def save_csv_report():
    """Day 11 skill reuse - CSV report"""
    filename = f"Day13_SNMP/snmp_report_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Device', 'CPU_%', 'CPU_Status', 'Memory_%', 'Memory_Status', 'Timestamp'])
        for r in results:
            writer.writerow([r[0], r[1], r[2], r[3], r[4], datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
    print(f"\n Report saved: {filename}")

if __name__ == "__main__":
    devices = ["demo.snmplabs.com", "R1-Core", "R2-DMZ", "R3-WAN"]

    print(f"Day 13: SNMP CPU+Memory Check at {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 75)

    start = time.time()
    threads = []

    for device in devices:
        t = threading.Thread(target=check_device_health, args=(device,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("-" * 75)
    print(f"Scanned {len(devices)} devices in {time.time() - start:.2f}s")

    critical_cpu = [r for r in results if r[2] == "CRITICAL"]
    critical_mem = [r for r in results if r[4] == "CRITICAL"]

    if critical_cpu or critical_mem:
        print(f" ALERT: {len(critical_cpu)} CPU CRITICAL, {len(critical_mem)} MEM CRITICAL")
    else:
        print(" All devices healthy")

    save_csv_report()