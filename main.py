from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import json
import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

# 🔑 Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

URL = "https://www.doenets.lk/examresults"

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

# ⚙️ Edge headless
edge_options = Options()
edge_options.add_argument("--headless=new")
edge_options.add_argument("--disable-gpu")
edge_options.add_argument("--log-level=3")

service = Service("msedgedriver.exe")
driver = webdriver.Edge(service=service, options=edge_options)

# 🚀 START MESSAGE
send_telegram("🟢 Script started and monitoring...")
print("🟢 Script started")

try:
    while True:
        print("\nChecking website...")

        driver.get(URL)
        time.sleep(12)

        dropdown = driver.find_element(By.CSS_SELECTOR, "select.form-control")
        options = dropdown.find_elements(By.TAG_NAME, "option")

        current = [opt.text for opt in options if opt.text != "Select the Exam"]

        print("Current exams:", current)

        # Load old data
        try:
            with open("data.json", "r") as f:
                old = json.load(f)
        except:
            old = []

        new_items = [x for x in current if x not in old]

        if new_items:
            message = "🚀 New exam update:\n" + "\n".join(new_items)
            print(message)
            send_telegram(message)
        else:
            print("No new updates")

        with open("data.json", "w") as f:
            json.dump(current, f)

        print("Waiting 60 seconds...")
        time.sleep(60)

# 🛑 STOP MESSAGE
except KeyboardInterrupt:
    print("🛑 Script stopped manually")
    send_telegram("🔴 Script stopped manually")

except Exception as e:
    print("Error:", e)
    send_telegram(f"⚠️ Script crashed: {e}")

finally:
    driver.quit()
    print("Driver closed")