import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    })

if __name__ == "__main__":
    send_message("🤖 Gold Macro AI\n\n✅ Version 0.1.0 Alpha is online!\n\nMonitoring economic events...")
