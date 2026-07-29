from flask import Flask, request, render_template, redirect, url_for, session
import datetime
import socket
import smtplib       # This is for email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'noc_secret_key_2026'

SENDER_EMAIL = "manager@gmail.com"
SENDER_PASSWORD = "klqn awgu shqz jmdz"
RECEIVER_EMAIL = "sandhiyarubi97@gmail.com"

last_status = {}    #To save status


def check_host(host, port=80):
    try:
        socket.create_connection((host, port), timeout=2)
        return "UP"
    except:
        return "DOWN"


def send_alert(service, status):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = f"NOC ALERT: {service} is {status}"

        body = f"Alert Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n Service: {service}\nStatus: {status}"
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print(f"Alert sent for {service}")
    except Exception as e:
        print(f"Email error: {e}")


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin123':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    global last_status
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    services = {
        "Google DNS": check_host("8.8.8.8", 53),
        "Cloudflare DNS": check_host("1.1.1.1", 53),
        "Youtube": check_host("youtube.com", 443),
        "GitHub": check_host("github.com", 443),
        "Test Service": check_host("999.999.999.999", 80),  # ivlo thappu IP
    }

    #Alert Logic : Email will come uf status changed
    for name, status in services.items():
        if name in last_status and last_status[name] != status:
            if status == "DOWN":
                send_alert(name, status)
        last_status[name] = status

    time = datetime.datetime.now() .strftime("%H:%M:%S")
    return render_template('dashboard.html', devices=services, time=time)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
