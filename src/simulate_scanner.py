import csv
from datetime import datetime
import random
import time

# Sample synthetic student roster
STUDENTS = [
    {"id": "STU1001", "name": "Aiden Smith"},
    {"id": "STU1002", "name": "Chloe Tremblay"},
    {"id": "STU1003", "name": "Liam Patel"},
    {"id": "STU1004", "name": "Sofia Garcia"},
    {"id": "STU1005", "name": "Noah Johnson"},
    {"id": "STU1006", "name": "Emma Wilson"},
]

FILENAME = "attendance_log.csv"


def initialize_csv():
  """Creates the CSV file with headers if it doesn't exist."""
  try:
    with open(FILENAME, mode="x", newline="", encoding="utf-8") as f:
      writer = csv.writer(f)
      writer.writerow(["StudentID", "StudentName", "ScanType", "Timestamp"])
  except FileExistsError:
    pass


def simulate_scan():
  """Simulates a random student scanning a QR code for check-in or check-out."""
  student = random.choice(STUDENTS)
  scan_type = random.choice(["Check-In", "Check-Out"])
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  with open(FILENAME, mode="a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([student["id"], student["name"], scan_type, timestamp])

  print(
      f"[{timestamp}] Simulated Scan -> {student['name']} ({student['id']})"
      f" completed a {scan_type}"
  )


if __name__ == "__main__":
  initialize_csv()
  print(
      "Starting QR Code Scan Simulator... Press Ctrl+C to stop.\nAppending new"
      f" scans to {FILENAME} every 5 seconds."
  )
  try:
    while True:
      simulate_scan()
      time.sleep(5)  # Simulates a scan every 5 seconds
  except KeyboardInterrupt:
      print("\nSimulation stopped.")