<h1 align="center">⚡ HCO-DataSnag</h1>
<p align="center">A powerful browser-based info grabber with live dashboard</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/Hackerscolonyofficial/HCO-DataSnag?color=green&style=flat-square" />
  <img src="https://img.shields.io/github/forks/Hackerscolonyofficial/HCO-DataSnag?style=flat-square" />
  <img src="https://img.shields.io/github/license/Hackerscolonyofficial/HCO-DataSnag?style=flat-square" />
  <img src="https://img.shields.io/badge/Made%20By-Azhar-red?style=flat-square" />
</p>

---

## 🧠 What is HCO-DataSnag?

HCO-DataSnag is a browser-based device fingerprinting tool built for **educational purposes**. Once the victim clicks a link, you receive detailed info including:

- ✅ IP Address, Browser, Device, OS
- ✅ RAM, Battery Level, GPU Info
- ✅ Timezone, Screen Size, Language
- ✅ Referrer, Connection Type
- ✅ And more...

All information appears **live on a hacker-style dashboard**, hosted on Replit.

---

## 🖥️ Live Dashboard Preview

![demo](demo.gif)

> Matrix-themed terminal UI with real-time updates.

---

## 🚀 Features

- 🌐 Cloudflare tunnel auto-link (Termux)
- 📱 Browser-based — no install or permission required
- ⚙️ Flask-based dashboard hosted on Replit
- 🧪 20+ device info parameters grabbed
- 👁️‍🗨️ Live victim log with timestamp
- 🔥 Dark hacker UI with HCO branding
- 📢 Footer: YouTube + credit

---

---

## 📦 Installation

### 🔹 1. Run in Termux:
```bash
pkg install python git cloudflared -y
pip install flask requests

cd termux_tool
python main.py
```
➡️ It will auto-start Flask + Cloudflare  
➡️ Copy the victim link from the terminal

---

### 🔹 2. Setup Dashboard on Replit:
- Create a new **Python Repl**
- Upload files from `dashboard/`
- Make sure `app.py` is set as main
- Install packages:
```bash
pip install flask
```
- Click **Run**
- Visit your live dashboard link to view victim logs

---

## ⚠️ Disclaimer

> This tool is made for **educational and awareness** purposes only.  
> Using it for unauthorized access or spying is illegal and unethical.

---

## ✨ Credits

> 💻 Code by [Azhar](https://github.com/Hackerscolonyofficial)  
> 📡 Powered by **Hackers Colony**

📺 YouTube: [@hackers_colony_tech](https://youtube.com/@hackers_colony_tech?si=pvdCWZggTIuGb0ya)

---
