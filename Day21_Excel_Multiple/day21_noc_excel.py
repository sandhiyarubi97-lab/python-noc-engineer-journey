import subprocess
import platform
import datetime
import requests
import time
import pandas as pd

BOT_TOKEN = "8570944481:AAGiosBN8QTOHcm6_1f9W0LR4ssXrWviv0Q"

#Send to multiple people. Add more chat IDs here
ADMIN_CHAT_IDS = ["8039943195"]

DEVICES = {
    "Google": "8.8.8.8",
    "Cloudflare": "1.1.1.1",
    "Router": "192.168.1.1",
    "Test-Down": "192.168.1.999"
}

LAST_STATUS = {}
LOG_FILE = "noc_log.xlsx"


def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(["ping", param, "1", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0


def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    for chat_id in ADMIN_CHAT_IDS:   #Loop and send to all admins
        requests.post(url, data={"chat_id": chat_id, "text": message})


def save_to_excel(timestamp, device, status):
    #Create new row and append to excel
    df_new = pd.DataFrame([[timestamp, device, status]], columns=['Time', 'Device', 'Status'])
    try:
        df_old = pd.read_excel(LOG_FILE)
        df = pd.concat([df_old, df_new], ignore_index=True)
    except:
        df = df_new
    df.to_excel(LOG_FILE, index=False)


def check_devices():
    alerts = []
    report = []
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for name, ip in DEVICES.items():
        current_status = "UP" if ping_host(ip) else "DOWN"
        emoji = "=" if current_status == "UP" else "$"
        report.append(f"{name}: {current_status} {emoji}")

        #Save every check to excel
        save_to_excel(current_time, name, current_status)

        #Check if status changed
        if name in LAST_STATUS and LAST_STATUS[name]!= current_status:
            alerts.append(f"STATUS CHANGE: {name} is now {current_status} {emoji}")
        LAST_STATUS[name] = current_status

        if alerts:
            msg = f"NOC ALERT - {current_time}\n\n" + "\n".join(alerts)
            send_telegram(msg)


def daily_report():
    now = datetime.datetime.now()
    if now.hour == 21 and now.minute == 0:   # 9 : 00 PM
        send_telegram(f"DAILY REPORT READY\nCheck '{LOG_FILE}' for today's full log.")

def run_noc_24x7():
    print("Day 21 NOC Bot Started. Logging to Excel.....")
    send_telegram("Day 21 NOC Bot Started! Logging to Excel + Multi-Admin Active.")
    check_devices()

    while True:
        time.sleep(60)   # 1 minute
        check_devices()
        daily_report()

run_noc_24x7()