# 🔥 AI Firewall Project — Intelligent Intrusion Detection System

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20App-lightgrey?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange?logo=scikit-learn)
![Platform](https://img.shields.io/badge/Tested%20On-Kali%20Linux-informational?logo=linux)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🧠 Overview

This is a real-time **AI-powered Firewall** built using Python, Scapy, and a Machine Learning model (Random Forest). It:
- Captures live network traffic
- Classifies packets as suspicious or safe
- Automatically blocks suspicious IPs using `iptables`
- Shows blocked IPs in a Flask web dashboard

---

## 🚀 Features

- 🔎 Real-time packet sniffing with Scapy  
- 🤖 ML classification of traffic (safe/suspicious)  
- 🔒 Automatic blocking of malicious IPs  
- 📝 Logging of blocked IPs in a `.log` file  
- 🌐 Flask dashboard to display blocked IPs  
- 🧪 Tested on Kali Linux

---

ai-firewall-project/

├── sniffer.py # Packet capture + dataset creation

├── train_model.py # Model training with Random Forest

├── firewall_model.pkl # Saved ML model

├── firewall.py # Real-time firewall with prediction + blocking

├── blocked_ips.log # Log of blocked IPs

├── dashboard.py # Flask web dashboard

├── traffic_dataset.csv # Captured packet data

├── .gitignore



📡 Step 2: Sniff Network Traffic       
sudo python3 sniffer.py
Captures 50 packets and saves to traffic_dataset.csv

🧠 Step 3: Train the ML Model
python3 train_model.py
Generates firewall_model.pkl

🔥 Step 4: Start the AI Firewall
sudo python3 firewall.py
Blocks suspicious IPs using your ML model

🌐 Step 5: Run Flask Dashboard
python3 dashboard.py
Then open in browser:  http://localhost:8080

🔓 Step 6: Unblock an IP (optional)
sudo iptables -D INPUT -s <blocked_ip> -j DROP

🙋 Author
Roshan Kumar
🔗 [https://www.linkedin.com/in/roshan-kumar-5306a5233/]
📧 [roshankumarji083@gmail.com]


📄 License
This project is under the MIT License.
⭐ If you like it, don’t forget to star the repo!

