import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Training data
data = {
    "source_port": [
        51520, 52100, 53000, 54000, 55000,
        4444, 4445, 4446, 4447, 4448,
        35000, 35001, 35002, 35003, 35004,
        53000, 53001, 53002, 53003, 53004
    ],

    "destination_port": [
        443, 443, 443, 80, 443,
        80, 80, 80, 80, 80,
        22, 23, 21, 22, 23,
        21, 21, 21, 21, 21
    ],

    "packet_count": [
        95, 120, 110, 100, 130,
        8500, 9000, 7800, 9200, 8800,
        600, 700, 550, 800, 650,
        450, 500, 470, 520, 490
    ],

    "bytes": [
        12000, 15400, 14000, 13500, 16000,
        950000, 1000000, 890000, 1100000, 970000,
        72000, 80000, 65000, 85000, 76000,
        55000, 60000, 57000, 62000, 59000
    ],

    "duration": [
        1.8, 2.5, 2.1, 2.0, 2.7,
        1.2, 1.0, 1.4, 1.1, 1.3,
        5.1, 4.8, 5.5, 4.9, 5.2,
        3.7, 3.5, 3.9, 3.6, 3.8
    ],

    "label": [
        "BENIGN", "BENIGN", "BENIGN", "BENIGN", "BENIGN",
        "DDoS", "DDoS", "DDoS", "DDoS", "DDoS",
        "PortScan", "PortScan", "PortScan", "PortScan", "PortScan",
        "BruteForce", "BruteForce", "BruteForce", "BruteForce", "BruteForce"
    ]
}

df = pd.DataFrame(data)

X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, predictions))

joblib.dump(model, "threat_detection_model.pkl")

print("\n✅ Model saved as threat_detection_model.pkl")