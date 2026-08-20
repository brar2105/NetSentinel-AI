import psycopg2


def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="cybersecurity_db",
        user="postgres",
        password="5432"
    )

    return connection


try:
    conn = get_connection()
    print("✅ PostgreSQL connected successfully!")

    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM network_traffic;")
    count = cursor.fetchone()[0]

    print(f"📊 Records in database: {count}")

    cursor.close()
    conn.close()

except Exception as e:
    print("❌ Database connection failed:")
    print(e)