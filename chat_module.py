import socket
import pyfiglet
import threading
import os
import subprocess as sp
from colorama import Fore,Style
os.system("clear")




def chat():
	afm=socket.AF_INET
	protocol=socket.SOCK_DGRAM
	ip="192.168.29.203"
	port_number=1234
	s=socket.socket(afm,protocol)
	s.bind((ip,port_number))
	os.system("tput reset")        
	print(pyfiglet.figlet_format("Chat App"))
	def recv():
		
		while True:
			x=s.recvfrom(1024)
			ip=x[1][0]
			msg=x[0].decode()
			print(Fore.BLUE)
			print((msg+" from "+ip).rjust(50,'-'))
			print(Style.RESET_ALL)

	def send():
		while True:
			x=input()
			if x=="exit":
				break
			else:
				s.sendto(x.encode(),('192.168.29.178',2224))
	
	
	
	x1=threading.Thread(target=recv)
	x2=threading.Thread(target=send)
	x1.start()
	x2.start()
	input()
	
