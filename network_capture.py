from scapy.all import sniff, IP, TCP, UDP
import psycopg2
import time

INTERFACE = "en0"

# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="cybersecurity_db",
    user="postgres",
    password="5432"
)

cursor = conn.cursor()

print("🔗 PostgreSQL connected!")
print(f"🔍 Capturing network traffic on {INTERFACE}...")
print("Press Ctrl+C to stop.\n")


def process_packet(packet):

    if IP not in packet:
        return

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst
    packet_size = len(packet)

    protocol = "OTHER"
    source_port = 0
    destination_port = 0

    if TCP in packet:
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

    elif UDP in packet:
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    # Store packet in PostgreSQL
    cursor.execute("""
        INSERT INTO network_traffic
        (source_ip, destination_ip, source_port,
         destination_port, protocol, packet_count,
         bytes, duration, label)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        source_ip,
        destination_ip,
        source_port,
        destination_port,
        protocol,
        1,
        packet_size,
        0.0,
        "UNKNOWN"
    ))

    conn.commit()

    print(
        f"📡 {source_ip} → {destination_ip} | "
        f"{protocol} | "
        f"{source_port} → {destination_port} | "
        f"{packet_size} bytes | Saved ✅"
    )


try:

    sniff(
        iface=INTERFACE,
        prn=process_packet,
        store=False
    )

except KeyboardInterrupt:

    print("\n🛑 Capture stopped.")

finally:

    cursor.close()
    conn.close()
    print("🔒 PostgreSQL connection closed.")