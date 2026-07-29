from flask import Flask, render_template, jsonify
import socket
import datetime

app = Flask(__name__)

def check_host(host, port=80):
    try:
        socket.create_connection((host, port), timeout=3)
        return "UP"
    except:
        return "DOWN"


@app.route('/')
def dashboard():
    services = {
        "Google": check_host("google.com"),
        "Cloudflare": check_host("cloudflare.com"),
        "Youtube": check_host("youtube.com"),
        "Router": check_host("8.8.8.8")
    }
    time = datetime.datetime.now().strftime("%H:%M:%S")
    return render_template('dashboard.html', services=services, time=time)

@app.route('/data')
def data():
    services = {
        "Google": check_host("google.com"),
        "Cloudflare": check_host("cloudflare.com"),
        "Youtube": check_host("youtube.com"),
        "Router": check_host("8.8.8.8")
    }
    time = datetime.datetime.now().strftime("%H:%M:%S")
    return jsonify(services=services, time=time)

if __name__ == "__main__":
    app.run(debug=True)