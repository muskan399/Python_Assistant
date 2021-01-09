import socket
import pyfiglet
import threading
import os
import subprocess as sp
from colorama import Fore,Style
os.system("clear")

def text_menu():
    os.system("clear")
    sp.getoutput("pulseaudio --start")
    os.system("tput setaf 2")
    os.system("figlet 'Helper Program'")
    greet='Hello I am Pluto,your technical helper'
    os.system("espeak-ng 'Hello I am Pluto your technical assistant'")
    print(greet)
    print("-------------------------------------------Here is the menu-------------------------------------\nEnter the option number")                          
    os.system("tput setaf 3")
    print("""
1. Cloud Services
2. Docker Services
3. Hadoop Services
4. Chat Service
5. Exit
    """)
    os.system("tput setaf 6")
    option=int(input())
    os.system("clear")
    if option==1:
        multi_cloud()
	
    elif option==2:
        docker()
               
    elif option==3:
        hadoop()
    elif option==4:
        chat()
            
    elif option==5:
        close()
    


def chat():
	os.system("tput reset")        
	print(pyfiglet.figlet_format("Chat App"))
	print("Welcome to app\n")
	afm=socket.AF_INET
	protocol=socket.SOCK_DGRAM
	ip="192.168.29.203"
	port_number=1234
	s=socket.socket(afm,protocol)
	s.bind((ip,port_number))
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
				
				text_menu()
				break
			else:
        			s.sendto(x.encode(),('192.168.29.178',2224))

	x1=threading.Thread(target=recv)
	x2=threading.Thread(target=send)
	x1.start()
	x2.start()
