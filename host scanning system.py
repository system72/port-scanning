import socket
import sys

h = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]

print("Your ip is: " + h)

port = []
openports = []

print("Would you like to scan home or other")
herty = raw_input("")
if herty == "home":
    host = '127.0.0.1'
else:
    host = raw_input("ip for scanning: ")

xh = input("first port scanned: ")
qwr = input("last port scanned: ")



sys.stdout.write('scanning')


for x in range(xh, qwr):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((host, x))

    if result == 0:
        port.append((x, " OPEN"))
        openports.append((x))
        sys.stdout.write('.')
    else:
        port.append((x, " closed"))
        sys.stdout.write('.')
        


sys.stdout.write('\n')
print("scanning done")
f = open('Open ports on scan.txt', 'w')
f.write(host + ": this is your scanned ip\n")
f.write("below is a list of all the ports that are open on your host\n")
f.write(' '.join(map(str, openports)))
for p in port:
    print(p)

f.close()
s.close()



import time

time.sleep(30)
