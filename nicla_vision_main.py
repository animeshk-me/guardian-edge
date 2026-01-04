# This work is licensed under the MIT license.
# Copyright (c) 2013-2023 OpenMV LLC. All rights reserved.
# https://github.com/openmv/openmv/blob/master/LICENSE
#
# Connect Example
#
# This example shows how to connect to a WiFi network.
# and sends the imu data to the host network

import network, time, socket
from machine import Pin, SPI, LED
from lsm6dsox import LSM6DSOX

from ulab import numpy as np

# a = np.array([[1, 2], [3, 4]])

SSID = "blinders"  # Network SSID
KEY = "father123"  # Network key
SAMPLE_RATE_HZ = 50  # Sample rate in Hz

# Init wlan module and connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, KEY)

red_led = LED("LED_RED"); green_led = LED('LED_GREEN')
timeout = 5
while not wlan.isconnected() and timeout > 0:
    print('Trying to connect to "{:s}"...'.format(SSID))
    time.sleep_ms(1000)
    timeout -= 1

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
PC_IP = "10.56.151.144"
PORT = 5005


circular_buffer = np.zeros((200,6))
is_buffer_full = False


# return the difference between the windows [head1, head1+150] and [head2, head2+150]
def get_diff_window(circular_buffer, head1, head2):
    diff_array = np.zeros((150, 6))
    for i in range(150):
        diff_array[i] = circular_buffer[(head2+i)%200] - circular_buffer[(head1+i)%200]
    return diff_array

# return circular distance between head1 and ptr
def get_dist(head1, ptr):
    if ptr >= head1:
        return ptr - head1
    else:
        return (200 - head1) + ptr

def compute_stats(diff_buff):
    max_stat = np.max(diff_buff, axis=0)
    min_stat = np.min(diff_buff, axis=0)
    mean_stat = np.mean(diff_buff, axis=0)
    return max_stat, min_stat, mean_stat
    
def score(ay_min):
    if ay_min <= -0.6363520100712776:
        return 1.0
    else:
        return 0.0

def imu_data():
    print('Now collecting the IMU data')
    spi = SPI(5)
    cs = Pin("PF6", Pin.OUT_PP, Pin.PULL_UP)
    lsm = LSM6DSOX(spi, cs)

    print("Device,Timestamp,Ax,Ay,Az,Gx,Gy,Gz")

    sample_interval_ms = int(1000 / SAMPLE_RATE_HZ)
    
    ptr = 0
    head1 = 0
    head2 = 50
    while True:
        start_time = time.ticks_ms()
        a = lsm.accel()  # Returns (x, y, z)
        g = lsm.gyro()   # Returns (x, y, z)
        # ts = start_time
        circular_buffer[ptr] = np.array([a[0], a[1], a[2], g[0], g[1], g[2]]);

        # Format for terminal/Excel
        # data = "B, %d, %f, %f, %f, %f, %f, %f" % (ts,
        #     a[0], a[1], a[2],
        #     g[0], g[1], g[2])
        
        # print(data)
        if (get_dist(head1, ptr) == 199):
            diff_window = get_diff_window(circular_buffer, head1, head2)
            (max_stat, min_stat, mean_stat) = compute_stats(diff_window)
            data =  "A,%f" %  (score(min_stat[1]))
            # data = "B, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f" % (
            #     max_stat[0], min_stat[0], mean_stat[0],
            #     max_stat[1], min_stat[1], mean_stat[1],
            #     max_stat[2], min_stat[2], mean_stat[2],
            #     max_stat[3], min_stat[3], mean_stat[3],
            #     max_stat[4], min_stat[4], mean_stat[4],
            #     max_stat[5], min_stat[5], mean_stat[5])
            
            head1 = head2
            head2 = (head2 + 50) % 200
            print("got data: ", data)            
            client.sendto(data.encode(), (PC_IP, PORT))
            
        ptr = (ptr + 1) % 200
        elapsed = time.ticks_diff(time.ticks_ms(), start_time)
        sleep_time = sample_interval_ms - elapsed
        if sleep_time > 0:
            time.sleep_ms(sleep_time)

if wlan.isconnected() == False:
    print('Failed to connect to Wi-Fi')
    red_led.on()
    while True:
        pass
else:
# We should have a valid IP now via DHCP
    print("WiFi Connected ", wlan.ifconfig())
    green_led.on()
    # time.sleep(1)
    # green_led.off()
    imu_data()
