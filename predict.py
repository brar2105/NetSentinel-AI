import psycopg2
import joblib
import pandas as pd


# Load trained model
model = joblib.load("threat_detection_model.pkl")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="cybersecurity_db",
    user="postgres",
    password="5432"
)

cursor = conn.cursor()

# Get traffic records
cursor.execute("""
    SELECT id, source_port, destination_port,
           packet_count, bytes, duration
    FROM network_traffic
    ORDER BY id
""")

records = cursor.fetchall()

print("\n🔍 Threat Detection Results")
print("-" * 50)

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

    print(
        f"Traffic ID: {traffic_id} "
        f"→ Prediction: {prediction}"
    )


cursor.close()
conn.close()