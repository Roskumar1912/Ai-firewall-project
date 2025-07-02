from scapy.all import sniff
import pandas as pd
import pickle
import os

# 🔐 Trained ML model load karo
with open("firewall_model.pkl", "rb") as f:
    model = pickle.load(f)

def process_packet(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        proto = packet["IP"].proto

        # ML model se prediction lo
        prediction = model.predict([[proto]])

        if prediction[0] == 1:
            print(f"🚨 Suspicious Packet Detected from {src_ip} | Protocol: {proto}")

            # ❌ Block karo IP ko
            block_command = f"iptables -A INPUT -s {src_ip} -j DROP"
            os.system(block_command)
            print(f"⛔ Blocked IP: {src_ip}")

            # 📜 Log file me entry karo
            with open("blocked_ips.log", "a") as log_file:
                log_file.write(f"{src_ip},Protocol:{proto}\n")

        else:
            print(f"✅ Normal Packet from {src_ip} | Protocol: {proto}")

# 🔍 Start monitoring
print("🔁 Real-time packet monitoring started... Press Ctrl+C to stop.")
sniff(prn=process_packet, store=0)
