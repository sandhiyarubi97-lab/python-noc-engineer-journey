import requests

BOT_TOKEN = "8570944481:AAGiosBN8QT0Hcm6_1f9W0LR4ssXrWviv0Q"
CHAT_ID = "8039943195"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
data = {"chat_id": CHAT_ID, "text": "🔥 TEST: If you see this, NOC Bot is working!"}

print("Sending to:", CHAT_ID)
r = requests.post(url, data=data)

print("Status Code:", r.status_code)
print("Full Response:", r.json())