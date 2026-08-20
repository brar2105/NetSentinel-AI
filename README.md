# 🛡️ NetSentinel AI

NetSentinel AI is an AI-powered network threat detection system designed to monitor and analyze live network traffic. The system captures network packets, aggregates them into flows, extracts relevant network features, and uses Machine Learning to classify network activity as **Benign, DDoS, Brute Force, or Port Scan**.

The system works through the terminal and stores processed network traffic and prediction results in **PostgreSQL**.

## What Are We Building?

NetSentinel AI is designed as a network security monitoring system where **live network traffic, packet capture, flow aggregation, Machine Learning, and database storage work together** for automated threat analysis.

The system monitors traffic from the currently active network interface and can analyze traffic from different network connections such as Wi-Fi or mobile hotspot.

## What Has Been Implemented?

- **Live Packet Capture** — Captures network packets using Scapy.
- **Flow Aggregation** — Groups packets into meaningful network flows.
- **Feature Extraction** — Extracts IP addresses, ports, protocols, packet counts, and byte statistics.
- **Threat Classification** — Uses Machine Learning to classify network traffic.
- **Threat Categories** — Supports Benign, DDoS, Brute Force, and Port Scan labels.
- **PostgreSQL Integration** — Stores network flows and prediction results.
- **Terminal-Based Detection** — Displays captured traffic and predictions directly in the terminal.

## 🔄 System Workflow


              Live Network Traffic
                       ↓
                📡 Scapy Capture
                       ↓
                Flow Aggregation
                       ↓
                Feature Extraction
                       ↓
                🤖 ML Prediction
                       ↓
              Threat Classification
                       ↓
                 PostgreSQL

When network traffic is captured, the system extracts relevant features from packets and aggregates them into network flows. These features are passed to the Machine Learning model, which predicts the corresponding traffic label. The processed flow and prediction are then stored in PostgreSQL.

🛠️ Technologies Used
Programming & Data Processing
Python
Pandas
NumPy
Network Security
Scapy
TCP/IP
UDP
Machine Learning
Machine Learning — Network traffic classification and threat prediction.
Database
PostgreSQL
Development Tools
Git
GitHub
VS Code
Python Virtual Environment
🛡️ Threat Categories
Label	Description
BENIGN	Normal network traffic
DDoS	Potential DDoS activity
BruteForce	Potential brute-force activity
PortScan	Potential port scanning activity
🖥️ Terminal Output

NetSentinel AI provides network traffic information and prediction results directly through the terminal.

Example:

📡 Network Flow Detected


Source:      192.168.x.x
Destination: xxx.xxx.xxx.xxx
Protocol:    TCP
Ports:       50098 → 443
Bytes:       1304


🤖 Prediction: BENIGN

For suspicious traffic:

🚨 THREAT DETECTED


Source:      xxx.xxx.xxx.xxx
Destination: xxx.xxx.xxx.xxx
Protocol:    TCP


⚠️ Prediction: PortScan

🌐 Network Switching

NetSentinel AI analyzes traffic available through the active network interface.

For example:

Wi-Fi Network
      ↓
NetSentinel AI
      ↓
Traffic Analysis

After switching to a mobile hotspot:

Mobile Hotspot
      ↓
NetSentinel AI
      ↓
New Network Traffic Analysis
The same detection pipeline can be used to analyze traffic from the newly active network connection.

🗄️ Database

PostgreSQL is used to store processed network-flow information and prediction results.

The stored information can include:

* Source IP
* Destination IP
* Source Port
* Destination Port
* Protocol
* Packet Count
* Bytes
* Prediction Label

Example labels:

* BENIGN
* BruteForce
* DDoS
* PortScan
* 
🏗️ Project Architecture:- 
 Network Interface
       ↓
Packet Capture
       ↓
Flow Aggregation
       ↓
Feature Extraction
       ↓
ML Prediction
       ↓
Threat Classification
       ↓
PostgreSQL Database

** Packet Capture Layer

Captures live packets from the active network interface using Scapy.

** Flow Aggregation Layer

Processes individual packets and combines them into network flows.

**Prediction Layer

Processes extracted features and uses the Machine Learning model to classify network traffic.

**Database Layer

Stores processed flows and prediction labels in PostgreSQL for further analysis.


⚠️ Disclaimer

NetSentinel AI is developed for educational, research, and authorized network security testing purposes only.

Only monitor and analyze network traffic for which you have proper authorization.


🎯 Conclusion

NetSentinel AI provides an automated approach to monitoring network traffic and identifying potential cyber threats using Machine Learning.

It combines live packet capture, flow analysis, threat classification, and PostgreSQL-based storage into a single network security solution.
