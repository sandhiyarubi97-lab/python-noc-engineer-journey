import subprocess
import platform
import datetime
import requests
import time

BOT_TOKEN = "8570944481:AAGiosBN8QTOHcm6_1f9W0LR4ssXrWviv0Q"
CHAT_ID = "8039943195"

# ==============Add real websites + my devices=======================
DEVICES = {
    "Google": "8.8.8.8",
    "Cloudflare": "1.1.1.1",
    "Router": "192.168.1.1",
    "Test-Down": "192.168.1.999"
}
# ==============This is dictionary will remember the last status===========
LAST_STATUS = {}


def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(["ping", param, "1", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0


def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})


def check_devices():
    alerts = []
    report = []

    for name, ip in DEVICES.items():
        current_status = "UP" if ping_host(ip) else "DOWN"
        emoji = "=" if current_status == "UP" else "$"
        report.append(f"{name}: {current_status} {emoji}")

        # Check if status changed
        if name in LAST_STATUS and LAST_STATUS[name] != current_status:
            alerts.append(f"STATUS CHANGE: {name} is now {current_status} {emoji}")

        # Update Memory
        LAST_STATUS[name] = current_status

    # Send alert only if something changed
    if alerts:
        msg = f"NOC ALERT - {datetime.datetime.now().strftime('%H:%M')}\n\n"
        msg += "\n".join(alerts) + "\n\n"
        msg += "Full Status:\n" + "\n".join(report)
        send_telegram(msg)
        print("ALERT SENT!")
    else:
        print(f"{datetime.datetime.now().strftime('%H:%M')} - All OK. NO Changes.")


def run_noc_24x7():
    print("NOC Bot Started. Monitoring every 5 minutes.....")
    send_telegram("NOC Bot Started! It will monitor and alert you 5 minutes.")

    while True:  # This makes it run forever===============
        check_devices()
        time.sleep(300)  # 300 seconds = 5 minutes

run_noc_24x7()
