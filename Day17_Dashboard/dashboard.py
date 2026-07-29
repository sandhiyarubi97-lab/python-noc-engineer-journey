from flask import Flask, render_template, request, redirect, session
import csv, os

app = Flask(__name__)
app.secret_key = 'noc123'


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            session['user'] = 'admin'
            return redirect('/dashboard')
        else:
            return "<h1 style='color:white'>Wrong password</h1>"
    return render_template('dashboard.html')


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')


    if not os.path.exists('snmp_report_latest.csv'):
        return "<h1 style='color:white'>CSV Not Found</h1>"

    devices = []
    with open('snmp_report_latest.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['CPU_%'] = int(row['CPU_%'])
            row['Memory_%'] = int(row['Memory_%'])
            devices.append(row)

    # history for trend chart
    history = {}
    for d in devices:
        history[d['Device']] = {
            'cpu': [d['CPU_%']],
            'time': [d['Timestamp']]
        }
        print("Devices:", devices)
        print("History:", history)

    return render_template('dashboard.html', devices=devices, history=history)


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)