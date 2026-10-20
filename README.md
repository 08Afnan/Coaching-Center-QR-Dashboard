# Real-Time Coaching Center QR Check-In & Analytics Dashboard

A lightweight, cost-effective portfolio project simulating a real-time IoT/QR code check-in and check-out system for coaching centers, built using **Python**, **CSV data logging**, and **Power BI**.

---

## 🏗️ Architecture & Design
Because enterprise cloud gateways (like Power Apps or Azure) often require paid licenses, this project implements a **local simulation pipeline** to mimic a real-time environment:
1. **The Mock Scanner (`src/simulate_scanner.py`):** A Python script that randomly simulates student QR scans (Check-In/Check-Out) with live timestamps.
2. **The Data Ledger (`data/attendance_log.csv`):** Acts as the central database where incoming scan events are appended.
3. **The Analytics Engine (`powerbi/`):** Power BI Desktop connects to the data source and uses custom DAX measures to calculate live metrics and peak traffic hours.

---

## 🚀 Key Features
* **Live Status Tracking:** Tracks which students are currently inside versus checked out.
* **Automated Data Feed:** Python script continuously pushes live timestamped events to simulate front-desk scans.
* **Advanced DAX Measures:** Calculates real-time occupancy and daily traffic patterns using time intelligence and context transition functions.
* **Cost-Optimized Architecture:** Achieves real-time analytical workflows entirely locally without paid cloud subscriptions.

---

## 🛠️ How to Run This Project

### 1. Run the Python QR Simulator
Make sure you have Python installed, navigate to the `src/` folder, and run:
\`\`\`bash
python simulate_scanner.py
\`\`\`
*(This will generate and continuously update `attendance_log.csv` every 5 seconds. Press `Ctrl + C` to stop).*

### 2. Explore the Power BI Dashboard
1. Open `powerbi/coaching_dashboard.pbix` in **Power BI Desktop**.
2. Click **Refresh** on the Home ribbon to pull in the latest simulated scan logs.