import subprocess as sp
import pyttsx3
import os
import pyfiglet
from docker_module import docker
from hadoop_module import hadoop
from cloud_module import multi_cloud
from chat_module import chat



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
    #os.system("clear")
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
    



os.system("clear")
os.system("tput setaf 4")
sp.getoutput("dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y")
sp.getoutput("yum install figlet -y")
os.system("tput bold")
os.system("figlet 'Welcome !!'")
print("Please enter the choice for communication")
print("""
1. Text
2. Voice
      """)
ch=int(input())
os.system("clear")
sp.getoutput("pulseaudio --start")
if(ch==1):
    while True:
        text_menu();
        os.system("clear")
else:
    r=sr.Recognizer()
    print("Please Speak!!!!!")
    with sr.Microphone() as source:
        a=sp.getoutput("clear")
    print(a)
    audio=r.listen(source)
    ins=r.recognize_google(audio)
    print(ins)
