# 🎓 Exam Result Monitor (DOE Sri Lanka)

A simple Python automation tool that monitors the official Department of Examinations website and sends a Telegram notification when new exam results are published.

---

## 🚀 Features

* Monitors exam dropdown updates automatically
* Sends instant Telegram alerts when new results appear
* Runs continuously in the background
* Supports headless mode (no browser window)
* Lightweight and beginner-friendly

---

## 📌 How It Works

The script:

1. Opens the official exam results website
2. Reads the available exam list from the dropdown
3. Compares it with previously saved data
4. Detects any new updates
5. Sends a Telegram notification if a change is found

---

## 🧰 Requirements

Make sure you have:

* Python 3.8 or higher
* Microsoft Edge browser installed
* Edge WebDriver (matching your browser version)

---

## ⚙️ Installation Guide

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/exam-result-monitor.git
cd exam-result-monitor
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Download Edge WebDriver

1. Open Edge and go to:

   ```
   edge://settings/help
   ```
2. Note your version
3. Download matching driver from:
   https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
4. Extract and place `msedgedriver.exe` inside the project folder

---

### 4. Create a Telegram Bot

1. Open Telegram
2. Search for **BotFather**
3. Send:

   ```
   /start
   ```
4. Then:

   ```
   /newbot
   ```
5. Follow instructions and copy your **BOT TOKEN**

---

### 5. Get your Chat ID

1. Send a message (e.g. "hi") to your bot
2. Open this link in browser:

```
https://api.telegram.org/botYOUR_TOKEN/getUpdates
```

3. Find:

```
"chat":{"id":123456789}
```

4. Copy the number → this is your **CHAT ID**

---

### 6. Configure the script

Open `main.py` and update:

```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
```

---

## ▶️ Running the Application

### Run normally (with terminal logs)

```bash
python main.py
```

---

### Run silently (background mode)

```bash
pythonw main.py
```

This will run without opening a terminal window.

---

## 🔔 Notifications

You will receive Telegram messages when:

* The script starts
* A new exam result is detected
* The script stops or crashes

---

## ⏱ Check Interval

Default interval:

```python
time.sleep(60)
```

Recommended values:

* 60 seconds → balanced and safe
* 30 seconds → faster but may increase load
* below 30 seconds → not recommended

---

## 📁 Project Structure

```
exam-result-monitor/
│
├── main.py
├── requirements.txt
├── README.md
├── data.json
```

---

## ⚠️ Important Notes

* First run will not send notifications (it saves current data)
* Do not use very short intervals (may trigger blocking)
* Keep your BOT TOKEN private
* Internet connection is required

---

## 🔒 Security Notice

Do NOT upload your real BOT TOKEN or CHAT ID to GitHub.
Always replace them with placeholder values before publishing.

---

## 📌 Disclaimer

This project is intended for educational purposes only.
It monitors publicly available data from the official website.

---

## ⭐ Contribution

Feel free to fork the project and improve it.
Suggestions and improvements are welcome.
