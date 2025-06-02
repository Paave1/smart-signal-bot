from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("7753764629:AAGPqSzLV7PmJ0MTW1PAhzCQ7VEuSvpSTcw")
CHAT_ID = os.getenv("1187964712")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get("message", "⚠️ Пустое сообщение от TradingView")
    send_message(message)
    return "OK"

def send_message(text):
    url = f"https://api.telegram.org/bot{7753764629:AAGPqSzLV7PmJ0MTW1PAhzCQ7VEuSvpSTcw}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, json=payload, headers={"Content-Type": "application/json"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
