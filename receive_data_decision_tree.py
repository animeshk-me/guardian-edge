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
DATA_DIR = "imu_data"
DATA_DIR = "imu_data2"
# -----------------------------

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
 
print(f"Listening on UDP port {UDP_PORT}")

activity_map = {0: "falling", 1: "riding"}

def score(input):
    if input[4] <= -0.6363520100712776:
        var0 = [1.0, 0.0]
    else:
        var0 = [0.0, 1.0]
    return var0

print("Nicla Vision: Starting Real-time Inference...")

try:
    while True:
        data, addr = sock.recvfrom(1024)
        decoded = data.decode().strip()
        row = decoded.split(",")
        device = row[0]
        ax_max = float(row[1])
        ax_min = float(row[2])
        ax_mean = float(row[3])

        ay_max = float(row[4])
        ay_min = float(row[5])
        ay_mean = float(row[6])

        az_max = float(row[7])
        az_min = float(row[8])
        az_mean = float(row[9])

        gx_max = float(row[10])
        gx_min = float(row[11])
        gx_mean = float(row[12])

        gy_max = float(row[13])
        gy_min = float(row[14])
        gy_mean = float(row[15])

        gz_max = float(row[16])
        gz_min = float(row[17])
        gz_mean = float(row[18])

        if device == 'B':
            continue

        feature = [ax_max, ax_min, ax_mean, ay_max, ay_min, ay_mean,
                   az_max, az_min, az_mean, gx_max, gx_min, gx_mean,
                   gy_max, gy_min, gy_mean, gz_max, gz_min, gz_mean]
        prediction = score(feature)

        max_val = max(prediction)
        predicted_idx = prediction.index(max_val)
        predicted_activity = activity_map[predicted_idx]
        print("data", row)
        print("prediction: ", predicted_activity)

except KeyboardInterrupt:
    print("\nStopped. File saved.")
 
sock.close()