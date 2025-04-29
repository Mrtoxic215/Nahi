# Telegram Music Download Bot 🎵

A simple yet powerful Telegram bot that lets users download songs via JioSaavn search API.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-Free-green)

---

## 🚀 Features
- Search any song by typing its name.
- Instantly get a 320kbps high-quality download link.
- Lightweight and fast performance.
- Powered by unofficial JioSaavn API.

---

## 📸 Demo

> (You can add a screenshot of your bot here later!)

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Bot Token
- Open `bot.py`
- Replace:
```python
TOKEN = "YAHAN_APNA_BOT_TOKEN_DALO"
```
with your actual token from [@BotFather](https://t.me/BotFather).

### 4. Run the Bot
```bash
python bot.py
```

---

## 🧰 Requirements
- python-telegram-bot==20.8
- requests

(Automatically installed from `requirements.txt`.)

---

## ⚡ How It Works
- User sends a song name in chat.
- Bot searches using JioSaavn API.
- Bot returns the **song name + direct download link (320kbps)**.

---

## ⚠️ Notes
- This bot uses **unofficial APIs**. Availability depends on third-party services.
- If JioSaavn API is down, bot may temporarily not work.

---

## 📄 License
This project is **free** and open source.  
Feel free to copy, improve, or modify it!

---
