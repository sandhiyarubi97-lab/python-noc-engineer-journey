import subprocess
import platform
import datetime
import requests
import time
import pandas as pd
from flask import Flask, render_template_string  # NEW
import threading

BOT_TOKEN = "8570944481:AAGiosBN8QT0Hcm6_1f9W0LR4ssXrWviv0Q"
ADMIN_CHAT_IDS = ["8039943195"]

DEVICES = {
    "Google": "8.8.8.8",
    "Cloudflare": "1.1.1.1",
    "Router": "192.168.1.1",
    "Test-Down": "192.168.1.999"
}

LAST_STATUS = {}
LOG_FILE = "noc_log.xlsx"
app = Flask(__name__)  # Flask Web Server


def ping_host(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    result = subprocess.run(["ping", param, "1", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0


def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    for chat_id in ADMIN_CHAT_IDS:
        requests.post(url, data={"chat_id": chat_id, "text": message})


def send_telegram_file(file_path):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
    for chat_id in ADMIN_CHAT_IDS:
        with open(file_path, 'rb') as doc:
            files = {'document': doc}
            data = {'chat_id': chat_id, 'caption': f"📊 Daily NOC Report - {datetime.date.today()}"}
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
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for name, ip in DEVICES.items():
        current_status = "UP" if ping_host(ip) else "DOWN"
        save_to_excel(current_time, name, current_status)

        if name in LAST_STATUS and LAST_STATUS[name] != current_status:
            emoji = "✅" if current_status == "UP" else "🚨"
            alerts.append(f"⚠️ STATUS CHANGE: {name} is now {current_status} {emoji}")

        LAST_STATUS[name] = current_status

    if alerts:
        msg = f"🚨 NOC ALERT - {current_time}\n\n" + "\n".join(alerts)
        send_telegram(msg)


def monitor_loop():
    print("Monitor Started")
    send_telegram("🤖 Day 23 NOC Bot + Web Dashboard Started!")
    check_devices()
    while True:
        time.sleep(60)  # Check every 1 min
        check_devices()
        daily_report()


def daily_report():
    now = datetime.datetime.now()
    if now.hour == 21 and now.minute == 0:
        send_telegram(f"📊 Sending Today's NOC Report...")
        time.sleep(2)
        send_telegram_file(LOG_FILE)


# WEB DASHBOARD PAGE
@app.route('/')
def dashboard():
    html = """
    <html>
    <head><title>NOC Dashboard</title>
    <meta http-equiv="refresh" content="10"> <!-- Auto refresh every 10s -->
    <style>
        body {font-family: Arial; background: #111; color: white; text-align: center;}
       .device {display: inline-block; margin: 20px; padding: 20px; width: 200px; border-radius: 15px;}
       .up {background: green;}
       .down {background: red;}
        h1 {color: #00ff00;}
    </style>
    </head>
    <body>
        <h1>🚨 NOC DASHBOARD 🚨</h1>
        <p>Last Updated: {{time}}</p>
        {% for name, status in devices.items() %}
        <div class="device {{status | lower}}">
            <h2>{{name}}</h2>
            <h3>{{status}}</h3>
        </div>
        {% endfor %}
        <audio id="alertSound" src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" preload="auto"></audio>

<script>
let wasDown = false; 

function checkForAlert() {
    let downDevices = document.querySelectorAll('.device.down').length;
    
    if (downDevices > 0 && wasDown == false) {
        document.getElementById('alertSound').play(); 
        wasDown = true;
    }
    if (downDevices == 0) {
        wasDown = false; // ellam UP aana reset aagidum
    }
}

// Page load aana udane check pannum
window.onload = checkForAlert;
// 5 sec ku oru thadava check pannum
setInterval(checkForAlert, 5000);
</script>
    </body>
    </html>
    """
    return render_template_string(html, devices=LAST_STATUS, time=datetime.datetime.now().strftime('%H:%M:%S'))


if __name__ == '__main__':
    # Run monitor in background thread
    thread = threading.Thread(target=monitor_loop)
    thread.daemon = True
    thread.start()

    # Run Flask Web Server
    print("Starting Web Dashboard on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000)