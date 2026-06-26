from netmiko import ConnectHandler, NetMikoTimeoutException
import logging
import time
from datetime import datetime

#1. Setup logging - runs only once.
logging.basicConfig(
    filename='router_uptime.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

router = {
    'device_type': 'cisco_ios',
    'host': 'sandbox-iosxe-latest-1.cisco.com',
    'port': 8181,
    'username': 'developer',
    'password': 'C1sco12345',
    'secret': 'C1sco12345'
}
print("Day 10 : Logging started. Check router_uptime.log file")
logging.info("Day 10 :Script started")


def check_uptime():
    try:
        logging.info(f"Connecting to {router['host']}")
        conn = ConnectHandler(**router)
        uptime = conn.send_command('show version | include uptime')
        conn.disconnect()

        #2. Replace print with logging
        logging.info(f"uptime check success: {uptime.strip()}")
        print(f"Logged to file: {uptime.strip()}")
        return True

    except NetMikoTimeoutException as e:
        #3. Log ErrorS too -NOC needs this
        error_msg = f"TCP Connection to device failed. Host:{router['host']}:{router['port']}"
        logging.error(error_msg)  # Don't pass e directly.It has new lines
        print(f"NOC Alert: {error_msg}")
        print("[Mock mode] Router uptime: 2 Days, 3 hours, 15 minutes")
        logging.info("Mock Mode: router uptime: 2 days, 3 hours, 15 minutes")
        return False

    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")    # convert to string
        print(f"Error: {str(e)}")
        return False


if __name__ == '__main__':
    try:
        while True:
            check_uptime()
            time.sleep(60)   # 1 min once check
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user")
        print("\nMonitoring stopped")


