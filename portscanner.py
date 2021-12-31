#!/bin/python3
import sys
import socket
from datetime import datetime
# Argv Count Checking
if len(sys.argv)==2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Syntax is Incorrect")
	print("Correct Syntax : python3 portscanner.py 127.0.0.1")
	exit()
# Banner
print("-"*50)
print("Simple Port Scanner")
print("Starting Port Scanner ...")
print("Target : "+sys.argv[1])
print("Start Time : "+str(datetime.now()))
print("-"*50)
# Port Scan
count = 0
for port in range(0,65535):
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result==0:
			count += 1
			serviceName = socket.getservbyport(port)
			print("Port "+str(port)+" is open "+serviceName)
		s.close()
	except KeyboardInterrupt:
		print("Exiting")
	except socket.gaierror:
		print("Host Name is not valid or Not found")
	except OSError:
		print("Port "+str(port)+" is open ServiceNotFound")
	except socket.error as e:
		print("Could't connect to server")
		sys.exit()
print(f"Port scan done: total {count} ports are open ")