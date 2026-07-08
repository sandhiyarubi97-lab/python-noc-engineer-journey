from flask import Flask, render_template, request, redirect, url_for, session
import csv
import os
from functools import wraps

app = Flask(__name__)
app.secret_key = "noc_secret_123"

USERNAME = "admin"
PASSWORD = "password123"


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)

    return decorated_function


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    devices = []
    history = {}

    # 1. Latest data - Day13_SNMP folder la irundhu
    csv_path = "../Day13_SNMP/snmp_report_latest.csv"
    if os.path.exists(csv_path):
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                devices.append(row)

    # 2. History data - Day14_Dashboard folder la irukanum
    history_path = "snmp_history.csv"
    if os.path.exists(history_path):
        with open(history_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                device = row['Device']
                if device not in history:
                    history[device] = {'time': [], 'cpu': [], 'mem': []}
                history[device]['time'].append(row['Timestamp'])
                history[device]['cpu'].append(int(row['CPU_%']))
                history[device]['mem'].append(int(row['Memory_%']))

    print("History Data Sent:", history)  # Debug ku
    return render_template('dashboard.html', devices=devices, history=history)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)