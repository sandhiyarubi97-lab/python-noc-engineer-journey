from flask import Flask, render_template_string
import datetime

app = Flask(__name__)

# For testing - later we will connect this to real monitoring
LAST_STATUS = {
    "Google": "UP",
    "Cloudflare": "UP",
    "Router": "UP",
    "Test-Down": "DOWN"
}


@app.route('/')
def dashboard():
    html = """
    <html>
    <head>
        <title>NOC Dashboard</title>
        <meta http-equiv="refresh" content="10">
        <style>
            body {font-family: Arial; background: #111; color: white; text-align: center;}
            .device {display: inline-block; margin: 20px; padding: 20px; width: 200px; border-radius: 15px;}
            .up {background: green;}
            .down {background: red;}
            h1 {color: #00ff00;}
        </style>
    </head>
    <body>
        <h1>🚨 NOC DASHBOARD - ONLINE 🚨</h1>
        <p>Last Updated: {{time}}</p>

        {% for name, status in devices.items() %}
        <div class="device {{status | lower}}">
            <h2>{{name}}</h2>
            <h3>{{status}}</h3>
        </div>
        {% endfor %}
    </body>
    </html>
    """
    return render_template_string(html, devices=LAST_STATUS, time=datetime.datetime.now().strftime('%H:%M:%S'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)