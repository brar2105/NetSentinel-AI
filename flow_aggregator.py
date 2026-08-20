import psycopg2
from collections import defaultdict


conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="cybersecurity_db",
    user="postgres",
    password="5432"
)

cursor = conn.cursor()

print("🔄 Aggregating network packets into flows...\n")


# Group packets by connection
cursor.execute("""
    SELECT
        source_ip,
        destination_ip,
        source_port,
        destination_port,
        protocol,
        COUNT(*) AS packet_count,
        SUM(bytes) AS total_bytes
    FROM network_traffic
    GROUP BY
        source_ip,
        destination_ip,
        source_port,
        destination_port,
        protocol
    ORDER BY packet_count DESC
    LIMIT 100
""")

flows = cursor.fetchall()


for flow in flows:

    source_ip = flow[0]
    destination_ip = flow[1]
    source_port = flow[2]
    destination_port = flow[3]
    protocol = flow[4]
    packet_count = flow[5]
    total_bytes = flow[6]

    # Demo duration
    duration = 1.0

    cursor.execute("""
        INSERT INTO network_flows
        (
            source_ip,
            destination_ip,
            source_port,
            destination_port,
            protocol,
            packet_count,
            bytes,
            duration,
            prediction
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        source_ip,
        destination_ip,
        source_port,
        destination_port,
        protocol,
        packet_count,
        total_bytes,
        duration,
        "PENDING"
    ))

    print(
        f"Flow: {source_ip} → {destination_ip} | "
        f"{protocol} | "
        f"Packets: {packet_count} | "
        f"Bytes: {total_bytes}"
    )


conn.commit()

cursor.close()
conn.close()

print("\n✅ Flow aggregation completed!")