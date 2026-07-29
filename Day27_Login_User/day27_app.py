from flask import Flask, render_template, request, redirect, url_for, session
import datetime
import subprocess
import platform

app = Flask(__name__)
app.secret_key = "sandhiya_secret_123" # needed for login sessions

PASSWORD = "admin123" # change this later

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

# KEY FIX: Both / and /dashboard go to same page
@app.route('/')
@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    status = {}
    for name, ip in DEVICES.items():
        status[name] = ping_host(ip)

    return render_template('dashboard.html',
                           devices=status,
                           time=datetime.datetime.now().strftime('%H:%M:%S'),
                           show_login=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)