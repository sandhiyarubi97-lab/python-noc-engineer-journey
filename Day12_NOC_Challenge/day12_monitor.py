from netmiko import ConnectHandler
import time
import csv
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import logging

# --- Email Config - Same as Day 11 ---
SENDER_EMAIL = "yourgmail@gmail.com"
SENDER_PASSWORD = "your_app_password"
RECEIVER_EMAIL = "yourphone@gmail.com"

# --- Logging Setup ---
logging.basicConfig(filename='day12_noc.log', level=logging.INFO,
                    format='%(asctime)s -(levelname)s - %(message)s')


def send_email_alert(down_routers):
    subject = f"ALERT: {len(down_routers)} Router(s) DOWN"
    body = f"Time: {datetime.now()}\nDown Routers:\n"
    for r in down_routers:
        body += f"- {r['host']}: {r['error']}\n"
    body += "\nAction: Check devices immediately"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        logging.info(f"Alert sent for {len(down_routers)} routers")
    except Exception as e:
        logging.error(f"Email failed: {e}")


def check_router(device):
    try:
        with ConnectHandler(**device) as net_connect:
            uptime = net_connect.send_command('show version | include uptime')
            return {"status": "UP", "uptime": uptime, "error": ""}
    except Exception as e:
        return {"status": "DOWN", "uptime": "N/A", "error": str(e)}


# --- Main Logic ---
routers = []
with open('routers.txt', 'r') as f:
    for line in f:
        ip = line.strip()
        if ip:
            routers.append({
                'device_type': 'cisco_ios',
                'host': ip,
                'port': 22,
                'username': 'developer',
                'password': 'C1sco12345',
            })

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
report_data = []
down_routers = []

print(f"Scanning {len(routers)} routers at {timestamp}...")

for device in routers:
    result = check_router(device)
    report_data.append({
        "Timestamp": timestamp,
        "Router": device['host'],
        "Status": result['status'],
        "Uptime": result['uptime'],
        "Error": result['error']
    })

    if result['status'] == "DOWN":
        down_routers.append({"host": device['host'], "error": result['error']})

    print(f"{device['host']} : {result['status']}")

# --- Save CSV Report ---
csv_file = 'router_report.csv'
file_exists = False
try:
    with open(csv_file, 'r'):
        file_exists = True
except FileNotFoundError:
    pass

with open(csv_file, 'a', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["Timestamp", "Router", "Status", "Uptime", "Error"])
    if not file_exists:
        writer.writeheader()  # Write header only once
    writer.writerows(report_data)

logging.info(f"CSV report updated. Total: {len(routers)}, DOWN: {len(down_routers)}")

# --- Send 1 Email for all DOWN routers ---
if down_routers:
    send_email_alert(down_routers)
else:
    print("All routers UP. No alert sent.")

print(f"Report saved to {csv_file}")