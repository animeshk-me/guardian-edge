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

# activity_map = {0: "falling", 1: "riding"}

# def score(input):
#     if input[4] <= -0.6363520100712776:
#         var0 = [1.0, 0.0]
#     else:
#         var0 = [0.0, 1.0]
#     return var0

activity_map = {0: "falling", 1: "jerking", 2: "riding", 3: "Can't classify!!"}

def score(input):
    if input[0] <= 0.052062999457120895:
        if input[27] <= 3.784180521965027:
            if input[16] <= -1.0681155025959015:
                var0 = [0.0, 0.0, 1.0]
            else:
                var0 = [0.0, 1.0, 0.0]
        else:
            if input[12] <= 1.7700200080871582:
                var0 = [0.0, 1.0, 0.0]
            else:
                var0 = [0.0, 0.2916666666666667, 0.7083333333333334]
    else:
        if input[20] <= 0.06589902378618717:
            var0 = [0.0, 1.0, 0.0]
        else:
            var0 = [1.0, 0.0, 0.0]
    return var0

print("Nicla Vision: Starting Real-time Inference...")

recieved_from_A = False
recieved_from_B = False

try:
    while True:
        data, addr = sock.recvfrom(1024)
        decoded = data.decode().strip()
        row = decoded.split(",")
        print(row)
        device = row[0]
        is_shaking = float(row[1]) == 1.0

        if device == "A":
            recieved_from_A = True
            A_is_shaking = is_shaking

        elif device == "B":
            recieved_from_B = True
            B_is_shaking = is_shaking

        predicted_activity = "Can't classify!!"
        if recieved_from_A and recieved_from_B:
            if A_is_shaking and B_is_shaking:
                predicted_activity = "falling"
            elif A_is_shaking and not(B_is_shaking):
                predicted_activity = "jerking"
            elif not(A_is_shaking) and not(B_is_shaking):
                predicted_activity = "riding"
            
            print("data", row)
            print("prediction: ", predicted_activity)
            recieved_from_A = False
            recieved_from_B = False

        # ax_max = float(row[1])
        # ax_min = float(row[2])
        # ax_mean = float(row[3])

        # ay_max = float(row[4])
        # ay_min = float(row[5])
        # ay_mean = float(row[6])

        # az_max = float(row[7])
        # az_min = float(row[8])
        # az_mean = float(row[9])

        # gx_max = float(row[10])
        # gx_min = float(row[11])
        # gx_mean = float(row[12])

        # gy_max = float(row[13])
        # gy_min = float(row[14])
        # gy_mean = float(row[15])

        # gz_max = float(row[16])
        # gz_min = float(row[17])
        # gz_mean = float(row[18])


        # if device == "A":
        #     A_ax_max = ax_max
        #     A_ax_min = ax_min
        #     A_ax_mean = ax_mean
        #     A_ay_max = ay_max
        #     A_ay_min = ay_min
        #     A_ay_mean = ay_mean
        #     A_az_max = az_max
        #     A_az_min = az_min
        #     A_az_mean = az_mean
        #     A_gx_max = gx_max
        #     A_gx_min = gx_min
        #     A_gx_mean = gx_mean
        #     A_gy_max = gy_max
        #     A_gy_min = gy_min
        #     A_gy_mean = gy_mean
        #     A_gz_max = gz_max
        #     A_gz_min = gz_min
        #     A_gz_mean = gz_mean
        #     recieved_from_A = True

        # elif device == "B":
        #     B_ax_max = ax_max
        #     B_ax_min = ax_min
        #     B_ax_mean = ax_mean
        #     B_ay_max = ay_max
        #     B_ay_min = ay_min
        #     B_ay_mean = ay_mean
        #     B_az_max = az_max
        #     B_az_min = az_min
        #     B_az_mean = az_mean
        #     B_gx_max = gx_max
        #     B_gx_min = gx_min
        #     B_gx_mean = gx_mean
        #     B_gy_max = gy_max
        #     B_gy_min = gy_min
        #     B_gy_mean = gy_mean
        #     B_gz_max = gz_max
        #     B_gz_min = gz_min
        #     B_gz_mean = gz_mean
        #     recieved_from_B = True
        
        # if recieved_from_A and recieved_from_B:
        #     feature = [A_ax_max, A_ax_min, A_ax_mean, A_ay_max, A_ay_min, A_ay_mean,
        #             A_az_max, A_az_min, A_az_mean, A_gx_max, A_gx_min, A_gx_mean,
        #             A_gy_max, A_gy_min, A_gy_mean, A_gz_max, A_gz_min, A_gz_mean,
        #             B_ax_max, B_ax_min, B_ax_mean, B_ay_max, B_ay_min, B_ay_mean,
        #             B_az_max, B_az_min, B_az_mean, B_gx_max, B_gx_min, B_gx_mean,
        #             B_gy_max, B_gy_min, B_gy_mean, B_gz_max, B_gz_min, B_gz_mean]
        
        #     prediction = score(feature)
        #     max_val = max(prediction)
        #     predicted_idx = prediction.index(max_val)
        #     predicted_activity = activity_map[predicted_idx]
        #     print("data", row)
        #     print("prediction: ", predicted_activity)
        #     recieved_from_A = False
        #     recieved_from_B = False

except KeyboardInterrupt:
    print("\nStopped. File saved.")
 
sock.close()