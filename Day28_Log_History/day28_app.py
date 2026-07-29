from flask import Flask, render_template, request, redirect, url_for, session
import datetime
import subprocess
import platform
import json
import os

app = Flask(__name__)
app.secret_key = "sandhiya_secret_123"

PASSWORD = "admin123"
LOG_FILE = "status_log.json"

DEVICES = {
    "Google DNS": "8.8.8.8",
    "Cloudflare DNS": "1.1.1.1",
    "YouTube": "youtube.com",
    "GitHub": "github.com"
}

def ping_host(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]
    try:
        result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=3)
        return "UP" if result.returncode == 0 else "DOWN"
    except:
        return "DOWN"

def save_log(device_name, status):
    log = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            log = json.load(f)

    log.append({
        "device": device_name,
        "status": status,
        "time": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    # Keep only last 50 logs
    log = log[-50:]
    with open(LOG_FILE, 'w') as f:
        json.dump(log, f)

def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            return json.load(f)[-10:] # show last 10
    return []

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return render_template('dashboard.html', error="Wrong Password! Try: admin123", show_login=True)
    return render_template('dashboard.html', show_login=True)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/')
@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    status = {}
    any_down = False
    for name, ip in DEVICES.items():
        current_status = ping_host(ip)
        status[name] = current_status
        save_log(name, current_status)
        if current_status == "DOWN":
            any_down = True

    logs = load_log()
    return render_template('dashboard.html',
                           devices=status,
                           logs=logs,
                           time=datetime.datetime.now().strftime('%H:%M:%S'),
                           any_down=any_down,
                           show_login=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)