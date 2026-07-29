import subprocess
import platform
import datetime
import requests
import time
import pandas as pd

BOT_TOKEN = "8570944481:AAGiosBN8QTOHcm6_1f9W0LR4ssXrWviv0Q"
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
    for chat_id in ADMIN_CHAT_IDS:
        requests.post(url, data={"chat_id": chat_id, "text": "message"})


def send_telegram_file(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    for chat_id in ADMIN_CHAT_IDS:
        with open(file_path, 'rb') as doc:
            files = {'document': doc}
            data = {'chat_id': chat_id, 'caption': f"Daily NOC Report - {datetime.datetime.today()}"}
            requests.post(url, data=data, files=files)


def save_to_excel(timestamp, device, status):
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
        save_to_excel(current_time, name, current_status)

        if name in LAST_STATUS and LAST_STATUS[name] != current_status:
            alerts.append(f"STATUS CHANGE: {name} is now {current_status} {emoji}")

        LAST_STATUS[name] = current_status

    if alerts:
        msg = f"NOC ALERT - {current_time}\n\n" + "\n".join(alerts) + "\n\nFull Status:\n".join(report)
        send_telegram(msg)


def daily_report():
    now = datetime.datetime.now()
    #send report at 9 : 00 PM and 9 : 01 PM to avoid missing it....
    if now.hour == 21 and now.minute in [0,1]:
        send_telegram(f"Sending Today's NOC Report........")
        time.sleep(2)
        send_telegram_file(LOG_FILE)
        print("Daily Excel sent!")


def run_noc_24x7():
    print("Day 22 NOC Bot Started. Will send Excel at 9 PM...")
    send_telegram("Day 22 NOC Bot Started...")
    check_devices()

    while True:
        time.sleep(60)
        check_devices()
        daily_report()


run_noc_24x7()
