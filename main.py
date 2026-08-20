import os
import numpy as np
import tensorflow as tf
import cv2

from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix


# ==========================================
# NEXT-GENERATION AI CYBERSECURITY FRAMEWORK
# PHASE 1 - AI BASED THREAT DETECTION
# ==========================================

SEED = 42

np.random.seed(SEED)
tf.random.set_seed(SEED)

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


# Cybersecurity classes
ATTACK_TYPES = {
    0: "Normal",
    1: "DoS",
    2: "Brute Force",
    3: "Port Scan"
}


# Network traffic features
FEATURE_NAMES = [
    "packet_rate",
    "packet_size",
    "flow_duration",
    "failed_logins",
    "unique_ports",
    "bytes_per_second",
    "connection_count",
    "suspicious_score"
]


# ==========================================
# 1. GENERATE DEMO CYBERSECURITY DATASET
# ==========================================

def generate_dataset(samples_per_class=1000):

    rng = np.random.default_rng(SEED)

    all_x = []
    all_y = []

    # Average feature values for each class
    means = {

        # Normal traffic
        0: [
            45, 650, 1200, 1,
            8, 30000, 20, 0.10
        ],

        # Denial of Service
        1: [
            900, 300, 400, 2,
            12, 90000, 300, 0.85
        ],

        # Brute Force
        2: [
            80, 450, 900, 35,
            15, 25000, 60, 0.75
        ],

        # Port Scan
        3: [
            250, 200, 250, 1,
            250, 45000, 180, 0.70
        ]
    }


    # Variation of each feature
    stds = {

        0: [
            12, 120, 250, 1,
            3, 7000, 7, 0.05
        ],

        1: [
            180, 90, 120, 2,
            4, 15000, 70, 0.08
        ],

        2: [
            30, 100, 180, 10,
            5, 6000, 20, 0.08
        ],

        3: [
            70, 70, 100, 1,
            45, 9000, 50, 0.10
        ]
    }


    # Generate samples
    for label in means:

        x = rng.normal(
            loc=np.array(means[label]),
            scale=np.array(stds[label]),
            size=(
                samples_per_class,
                len(FEATURE_NAMES)
            )
        )

        # Remove negative values
        x = np.maximum(x, 0)

        y = np.full(
            samples_per_class,
            label
        )

        all_x.append(x)
        all_y.append(y)


    # Combine all classes
    X = np.vstack(all_x).astype(
        np.float32
    )

    y = np.concatenate(all_y).astype(
        np.int32
    )


    # Shuffle dataset
    indices = rng.permutation(
        len(X)
    )

    return X[indices], y[indices]


# ==========================================
# 2. BUILD AI MODEL
# ==========================================

def build_model(
    input_size,
    number_of_classes
):

    model = keras.Sequential([

        layers.Input(
            shape=(input_size,)
        ),

        layers.Dense(
            64,
            activation="relu"
        ),

        layers.Dropout(0.25),

        layers.Dense(
            32,
            activation="relu"
        ),

        layers.Dropout(0.15),

        layers.Dense(
            number_of_classes,
            activation="softmax"
        )
    ])


    model.compile(

        optimizer=keras.optimizers.Adam(
            learning_rate=0.001
        ),

        loss="sparse_categorical_crossentropy",

        metrics=["accuracy"]
    )


    return model


# ==========================================
# 3. OPENCV THREAT MONITORING DASHBOARD
# ==========================================

def create_dashboard(
    y_pred,
    accuracy
):

    width = 1000
    height = 650

    dashboard = np.ones(
        (
            height,
            width,
            3
        ),
        dtype=np.uint8
    ) * 245


    # Title
    cv2.putText(

        dashboard,

        "AI CYBERSECURITY THREAT MONITOR",

        (45, 60),

        cv2.FONT_HERSHEY_SIMPLEX,

        1.0,

        (30, 30, 30),

        2
    )


    # Accuracy
    cv2.putText(

        dashboard,

        f"Model Accuracy: {accuracy * 100:.2f}%",

        (45, 105),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.75,

        (30, 30, 30),

        2
    )


    # Count predictions
    counts = {}

    for label in ATTACK_TYPES:

        counts[label] = int(
            np.sum(
                y_pred == label
            )
        )


    y_position = 180


    for label, name in ATTACK_TYPES.items():

        text = (
            f"{name}: "
            f"{counts[label]}"
        )


        cv2.putText(

            dashboard,

            text,

            (70, y_position),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.7,

            (40, 40, 40),

            2
        )


        bar_length = min(

            650,

            max(
                20,
                counts[label] // 2
            )
        )


        cv2.rectangle(

            dashboard,

            (
                360,
                y_position - 22
            ),

            (
                360 + bar_length,
                y_position
            ),

            (80, 120, 200),

            -1
        )


        y_position += 75


    # Status
    cv2.putText(

        dashboard,

        "Status: Threat classification pipeline operational",

        (45, 535),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.68,

        (30, 30, 30),

        2
    )


    # Save dashboard
    output_path = os.path.join(

        OUTPUT_DIR,

        "phase1_threat_monitor.png"
    )


    cv2.imwrite(

        output_path,

        dashboard
    )


    return output_path


# ==========================================
# 4. MAIN PROGRAM
# ==========================================

def main():

    print("=" * 65)

    print(
        "NEXT-GENERATION AI CYBERSECURITY "
        "FRAMEWORK - PHASE 1"
    )

    print("=" * 65)


    # --------------------------------------
    # Dataset
    # --------------------------------------

    print(
        "\n[1] Generating cybersecurity dataset..."
    )


    X, y = generate_dataset()


    print(
        "Dataset shape:",
        X.shape
    )


    print(
        "Number of samples:",
        len(X)
    )


    # --------------------------------------
    # Data preprocessing
    # --------------------------------------

    print(
        "\n[2] Preprocessing data..."
    )


    X_train, X_test, y_train, y_test = (

        train_test_split(

            X,

            y,

            test_size=0.20,

            random_state=SEED,

            stratify=y
        )
    )


    scaler = StandardScaler()


    X_train = scaler.fit_transform(
        X_train
    ).astype(np.float32)


    X_test = scaler.transform(
        X_test
    ).astype(np.float32)


    print(
        "Training samples:",
        len(X_train)
    )


    print(
        "Testing samples:",
        len(X_test)
    )


    # --------------------------------------
    # Build model
    # --------------------------------------

    print(
        "\n[3] Building TensorFlow/Keras model..."
    )


    model = build_model(

        X_train.shape[1],

        len(ATTACK_TYPES)
    )


    model.summary()


    # --------------------------------------
    # Train model
    # --------------------------------------

    print(
        "\n[4] Training AI model..."
    )


    model.fit(

        X_train,

        y_train,

        validation_split=0.20,

        epochs=20,

        batch_size=32,

        verbose=1
    )


    # --------------------------------------
    # Evaluate model
    # --------------------------------------

    print(
        "\n[5] Evaluating model..."
    )


    loss, accuracy = model.evaluate(

        X_test,

        y_test,

        verbose=0
    )


    predictions = model.predict(

        X_test,

        verbose=0
    )


    y_pred = np.argmax(

        predictions,

        axis=1
    )


    print(
        "\nTest Loss:",
        round(loss, 4)
    )


    print(
        "Test Accuracy:",
        f"{accuracy * 100:.2f}%"
    )


    # --------------------------------------
    # Classification report
    # --------------------------------------

    print(
        "\nClassification Report:"
    )


    print(

        classification_report(

            y_test,

            y_pred,

            target_names=list(
                ATTACK_TYPES.values()
            ),

            digits=4
        )
    )


    # --------------------------------------
    # Confusion matrix
    # --------------------------------------

    print(
        "\nConfusion Matrix:"
    )


    print(

        confusion_matrix(

            y_test,

            y_pred
        )
    )


    # --------------------------------------
    # Save trained model
    # --------------------------------------

    model_path = os.path.join(

        OUTPUT_DIR,

        "cyber_threat_detector.keras"
    )


    model.save(
        model_path
    )


    # --------------------------------------
    # OpenCV dashboard
    # --------------------------------------

    print(
        "\n[6] Creating OpenCV dashboard..."
    )


    dashboard_path = create_dashboard(

        y_pred,

        accuracy
    )


    # --------------------------------------
    # Final output
    # --------------------------------------

    print("\n" + "=" * 65)

    print(
        "PHASE 1 COMPLETED SUCCESSFULLY"
    )

    print("=" * 65)


    print(
        "\nModel saved at:"
    )

    print(
        model_path
    )


    print(
        "\nOpenCV dashboard saved at:"
    )

    print(
        dashboard_path
    )


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":

    main()