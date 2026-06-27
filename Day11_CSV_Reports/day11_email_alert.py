import csv
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Day 11: Mock device data - later  we can use dat in real Netmiko
devices = [
    {"hostname": "R1", "uptime": "5 weeks, 2 days", "ios": "15.2(4)M1", "int_down": 0},
    {"hostname": "R2", "uptime": "2 days, 3 hours", "ios": "15.2(4)M1", "int_down": 2},
    {"hostname": "SW1", "uptime": "1 year, 4 months", "ios": "16.12.04", "int_down": 0},
]

# 1. Create reports folder
script_dir = os.path.dirname(os.path.abspath(__file__))
reports_dir = os.path.join(script_dir, "reports")
os.makedirs(reports_dir, exist_ok=True)

# 2. Generate CSV with timestamp
today = datetime.now().strftime("%Y-%m-%d_%H%M")
csv_filename = os.path.join(reports_dir, f"noc_report_{today}.csv")

critical_devices = []

with open(csv_filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Hostname", "Uptime", "IOS_Version", "Down_Interfaces", "Status"])

    for device in devices:
        status = "CRITICAL" if device["int_down"] > 0 else "OK"
        if status == "CRITICAL":
            critical_devices.append(device)

        writer.writerow([
            device["hostname"],
            device["uptime"],
            device["ios"],
            device["int_down"],
            status
        ])

print(f"✅ Report generated: {csv_filename}")

# 3. Email Alert Logic - NOC Standard
if critical_devices:
    print(f"⚠️  CRITICAL ALERT: {len(critical_devices)} devices DOWN")

    # building Email body
    email_body = "NOC Daily Health Check - CRITICAL DEVICES FOUND\n\n"
    for dev in critical_devices:
        email_body += f"Device: {dev['hostname']}\n"
        email_body += f"Uptime: {dev['uptime']}\n"
        email_body += f"Down Interfaces: {dev['int_down']}\n"
        email_body += f"Status: CRITICAL\n"
        email_body += "-" * 40 + "\n"

    email_body += f"\nFull report: {csv_filename}"

    # Mock email - without using real SMTP details
    print("\n" + "=" * 50)
    print("MOCK EMAIL ALERT")
    print("=" * 50)
    print(f"To: noc-team@company.com")
    print(f"Subject: [CRITICAL] NOC Alert - {len(critical_devices)} Devices DOWN")
    print(f"Body:\n{email_body}")
    print("=" * 50)

    # Real email code - Need App Password fro Gmail use
    # sender = "your-email@gmail.com"
    # password = "your-app-password"  # Not regular password!
    # receiver = "noc-team@company.com"
    #
    # msg = MIMEMultipart()
    # msg['From'] = sender
    # msg['To'] = receiver
    # msg['Subject'] = f"[CRITICAL] NOC Alert - {len(critical_devices)} Devices DOWN"
    # msg.attach(MIMEText(email_body, 'plain'))
    #
    # try:
    #     server = smtplib.SMTP('smtp.gmail.com', 587)
    #     server.starttls()
    #     server.login(sender, password)
    #     server.sendmail(sender, receiver, msg.as_string())
    #     server.quit()
    #     print("✅ Email sent successfully!")
    # except Exception as e:
    #     print(f"❌ Email failed: {e}")

else:
    print("✅ All devices OK - No alerts sent")

print("\n" + "-" * 50)
print("Day 11 Complete: CSV + Alert Logic Done")
