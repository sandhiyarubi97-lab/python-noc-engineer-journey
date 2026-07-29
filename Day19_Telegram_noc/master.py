import subprocess
import platform
import datetime
import requests

BOT_TOKEN = "8570944481:AAGiosBN8QTOHcm6_1f9W0LR4ssXrWviv0Q"
CHAT_ID = "8039943195"

DEVICES = {
    "Router": "192.168.1.1",
    "Server": "192.168.1.10",
    "Test-Down": "192.168.1.999"  # This one will trigger alert
}


def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(["ping", param, "1", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0


def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    r = requests.post(url, data={"chat_id": CHAT_ID, "text": message})
    print("Telegram Status:", r.status_code)


def run_noc():
    print("Starting NOC Scan...")
    alerts = []
    report = []
    for name, ip in DEVICES.items():
        status = "UP ✅" if ping_host(ip) else "DOWN 🚨"
        report.append(f"{name}: {status}")
        if "DOWN" in status: alerts.append(f"🚨 ALERT: {name} {ip} is DOWN")

    msg = f"NOC Report - {datetime.datetime.now().strftime('%H:%M')}\n\n"
    msg += "\n".join(alerts) + "\n\n" if alerts else "✅ All Systems OK\n\n"
    msg += "\n".join(report)
    send_telegram(msg)
    print("Check @Sandhiya_noc_bot now")


run_noc()