import time
import joblib
import psycopg2
import pandas as pd


MODEL_FILE = "threat_detection_model.pkl"


# Load ML model
model = joblib.load(MODEL_FILE)


# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="cybersecurity_db",
    user="postgres",
    password="5432"
)

cursor = conn.cursor()

print("🤖 AI Threat Detector Started")
print("🔍 Monitoring live network traffic...")
print("Press Ctrl+C to stop.\n")


try:

    while True:

        # Get recent unknown traffic
        cursor.execute("""
            SELECT
                id,
                source_port,
                destination_port,
                packet_count,
                bytes,
                duration
            FROM network_traffic
            WHERE label = 'UNKNOWN'
            ORDER BY id DESC
            LIMIT 50
        """)

        records = cursor.fetchall()

        for record in records:

            traffic_id = record[0]

            features = pd.DataFrame([{
                "source_port": record[1],
                "destination_port": record[2],
                "packet_count": record[3],
                "bytes": record[4],
                "duration": record[5]
            }])

            prediction = model.predict(features)[0]

            # Update database
            cursor.execute("""
                UPDATE network_traffic
                SET label = %s
                WHERE id = %s
            """, (prediction, traffic_id))

            conn.commit()

            print(
                f"Traffic ID: {traffic_id} "
                f"→ 🤖 Prediction: {prediction}"
            )

        time.sleep(2)


except KeyboardInterrupt:

    print("\n🛑 AI detector stopped.")


finally:

    cursor.close()
    conn.close()
    print("🔒 Database connection closed.")