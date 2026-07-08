import smtplib
import csv
import shutil  # NEW: copy panna
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

CSV_PATH = '../Day13_SNMP/snmp_report_latest.csv'  # CHANGED


def check_critical():
    critical_devices = []
    try:
        with open(CSV_PATH, 'r') as f:
            reader = csv.DictReader(f)
            print("CSV Columns:", reader.fieldnames)
            for row in reader:
                if row['CPU_Status'] == 'CRITICAL' or row['Memory_Status'] == 'CRITICAL':
                    critical_devices.append(row)
    except FileNotFoundError:
        print(f"ERROR: {CSV_PATH} not found. Run snmp_check.py first")
    return critical_devices


def send_email(critical_list):
    sender_email = "sandhiyarubi97@gmail.com"
    receiver_email = "manager_email@gmail.com"  # Manager mail
    password = "aocp pthu ralw krso"

    if not critical_list:
        print(" No critical devices. No email sent.")
        return

    body = f" NOC ALERT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    body += "Critical Devices Found:\n\n"
    for dev in critical_list:
        body += f"Device: {dev['Device']}\nIP: {dev['IP']}\n"
        body += f"CPU: {dev['CPU_%']}% - {dev['CPU_Status']}\n"
        body += f"Memory: {dev['Memory_%']}% - {dev['Memory_Status']}\n"
        body += f"Time: {dev['Timestamp']}\n" + "-" * 40 + "\n"
    body += "\nPlease take immediate action.\n\nNOC Automation System"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = f" NOC CRITICAL ALERT - {len(critical_list)} Device(s) Down"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print(f" Email sent! {len(critical_list)} critical device(s) reported.")
    except Exception as e:
        print(f" Email failed: {e}")


if __name__ == "__main__":
    critical = check_critical()
    send_email(critical)

    src = '../Day13_SNMP/snmp_report_latest.csv'
    dst = '../Day17_Dashboard/snmp_report_latest.csv'

    # NEW: Dashboard ku latest copy
    if os.path.exists(src):
        shutil.copy(src, dst)
        print("CSV copied to Dashboard folder")