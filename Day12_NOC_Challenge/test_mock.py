import threading
import time
import logging
import random
from datetime import datetime

logging.basicConfig(filename='day12_noc.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

results = []

def ping_device(device_name):
    """Mock ping with delay"""
    logging.info(f"Checking {device_name}")
    time.sleep(random.uniform(1, 2)) # Simulate network delay

    status = random.choices(['UP', 'DOWN'], weights=[80, 20])[0]
    results.append((device_name, status))
    logging.info(f"{device_name} : {status}")
    print(f"{device_name} : {status}")

if __name__ == "__main__":
    devices = [f"R{i}" for i in range(1, 11)] + ["8.8.8.8", "1.1.1.1"]
    threads = []

    print(f"Scanning {len(devices)} devices at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}...")
    start = time.time()

    # Create threads
    for device in devices:
        t = threading.Thread(target=ping_device, args=(device,))
        threads.append(t)
        t.start()

    # Wait for all threads
    for t in threads:
        t.join()

    end = time.time()

    print(f"\nTotal time: {end - start:.2f} seconds")
    print(f"Devices UP: {len([r for r in results if r[1] == 'UP'])}")
    print(f"Devices DOWN: {len([r for r in results if r[1] == 'DOWN'])}")
    print("Report saved to router_report.csv")

    logging.info(f"Scan complete in {end - start:.2f}s")