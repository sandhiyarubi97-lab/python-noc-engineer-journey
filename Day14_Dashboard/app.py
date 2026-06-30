from flask import Flask, render_template
import csv, glob, os

app = Flask(__name__)

@app.route('/')
def dashboard():
    csv_files = glob.glob('Day13_SNMP/snmp_report_*.csv')
    if not csv_files:
        return "No reports. Run Day 13 first."

    latest = max(csv_files, key=os.path.getctime)
    devices = list(csv.DictReader(open(latest)))
    return render_template('dashboard.html', devices=devices)

if __name__ == '__main__':
    app.run(debug=True)