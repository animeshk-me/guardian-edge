import socket
import csv
import os
from datetime import datetime
import time
 
# -----------------------------
# CONFIG
# -----------------------------
UDP_IP = "0.0.0.0"
UDP_PORT = 5005
# DATA_DIR = "imu_data"
DATA_DIR = "jerking_data"
# -----------------------------

os.makedirs(DATA_DIR, exist_ok=True)
# activity = input("Enter activity label (e.g., riding, turning, falling): ")
activity = "jerking"
filename = f"{activity}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
filepath = os.path.join(DATA_DIR, filename)
 
f = open(filepath, "w", newline="")
writer = csv.writer(f)
# writer.writerow(["Device", "timestamp", "ax", "ay", "az", "gx", "gy", "gz", "activity"])

writer.writerow(["device","ax_max","ax_min","ax_mean","ay_max","ay_min","ay_mean","az_max","az_min","az_mean","gx_max","gx_min","gx_mean","gy_max","gy_min","gy_mean","gz_max","gz_min","gz_mean","activity"])
 
duration_seconds = 4  # 2 minutes
print('recording will start in 5 seconds')
# for i in range(5):
#     print(i)
#     time.sleep(1)
start_time = time.time() 

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
 
print(f"Listening on UDP port {UDP_PORT}")
print(f"Saving to {filepath}")

print('recording start')

try:
    while (time.time() - start_time) < duration_seconds:
        data, addr = sock.recvfrom(1024)
        decoded = data.decode().strip()
        row = decoded.split(",")
        row.append(activity)
        writer.writerow(row)
        print(row)
except KeyboardInterrupt:
    print("\nStopped. File saved.")
 
sock.close()