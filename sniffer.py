from scapy.all import sniff
import pandas as pd

packets = []

def process_packet(packet):
    if packet.haslayer("IP"):
        src = packet["IP"].src
        dst = packet["IP"].dst
        proto = packet["IP"].proto
        packets.append([src, dst, proto])
        print(f"{src} → {dst} | Protocol: {proto}")

# Capture 50 packets
sniff(prn=process_packet, count=50)

# Save to CSV
df = pd.DataFrame(packets, columns=["Source", "Destination", "Protocol"])
df.to_csv("traffic_dataset.csv", index=False)
print("✅ Packets saved to traffic_dataset.csv")
