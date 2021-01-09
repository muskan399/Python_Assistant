import subprocess as sp
import pyttsx3
import os
import pyfiglet
<<<<<<< HEAD
from docker_module import docker
from hadoop_module import hadoop
from cloud_module import multi_cloud
from chat_module import chat
=======


#launch os function
def launchOs():
	image = input("\n\t\tType the image name with version (like, unbuntu:14.04): ")
	#set name for os
	osname =input("\t\tSet your os name: ")
	#Create new Operating System 
	output = sp.getstatusoutput("docker run -d -it --name {} {} ".format(osname,image))
	if output[0] == 0:
		os.system("tput setaf 2")
		print("\t\tContainer {} successfully launched ".format(osname))
		os.system("tput setaf 7")
		input("press Enter Key to continue...") 
	
def menu():
	result=pyfiglet.figlet_format("   D O C K E R")
	print(result)
	op = input('''
\t------------------------------------------------
\t|\tPress 1: Install Docker                |
\t|\tPress 2: Download an OS image          |
\t|\tPress 3: See existing Images:          |
\t|\tPress 4: Launch new container          |
\t|\tPress 5: See all running Os            |
\t|\tPress 6: See all launch Os             |
\t|\tPress 7: Start or Stop container       |
\t|\tPress 8: Get the  docker terminal      |
\t|\tPress 9: Delete an existing Image      |
\t|\tPress 10: Clone an Image               |
\t|\tPress 11: Remove an existing container |
\t|\tPress 12: Remove all containers        | 
\t|\tPress 13: Back to main menu            |
\t|\tPress 14: Exit                         |
\t------------------------------------------------
\n\t\t>> ''')
	return op


#colored success message
def success(msg):
	os.system("tput setaf 2")
	print("\t\t{}".format(msg))
	os.system("tput setaf 7")
	input("press Enter Key to continue...") 




def close():
    sp.getoutput("pulseaudio --start")
    os.system("tput reset")
    os.system("figlet 'Thank You'")
    os.system("espeak-ng 'Thank you for using my services'")
    exit()

#main function
def docker():
	option = menu()
	if option == '1':
		os.system("touch /etc/yum.repos.d/docker-ce.repo")
		os.system("echo '[docker]\nbaseurl =https://download.docker.com/linux/centos/7/x86_64/stable/packages/\n gpgcheck=0' > /etc/yum.repos.d/docker-ce.repo")

		install = sp.getstatusoutput("yum install -y docker-ce --nobest")
		print("\n{}".format(install[1]))
	
	elif option == '2':
		pullImg = sp.getstatusoutput("docker image pull {}".format(input("Enter the Image name: ")))
		print(pullImg[1])
	
	elif option == '3':
		availableImages = sp.getstatusoutput("docker images ")
		print("\n{}".format(availableImages[1]))

	elif option == '4':
		launchOs()

	elif option == '5':
		runningOs = sp.getstatusoutput("docker ps ")
		print("\n{}".format(runningOs[1]))

	elif option == '6':
		launchedOs = sp.getstatusoutput("docker container ps -a")
		print("\n{}".format(launchedOs[1]))

	elif option == '7':
		op = input('''\t\tPress 1: Start\n\t\tPress 2: Stop\n''')
		if op == '1':
			output = sp.getstatusoutput("docker start {} ".format(input("\t\tEnter container name: ")))
			if output[0] == 0:
				success("container started successfully")

		elif op == '2':
			output = sp.getstatusoutput("docker stop {} ".format(input("\t\tEnter container name: ")))
			if output[0] == 0:
				success("container stopped successfully")

	elif option =='8':
		print("\t\tType 'exit' for getout from docker terminal of " )
		os.system("docker start {0} && tput setaf 6 && docker exec -it {0} /bin/bash ".format(input("\t\tOS name: ")))
		os.system("tput setaf 7")
		
	elif option == '9':
		rmImage = input("\t\tEnter image name/id: ")
		output= sp.getstatusoutput("docker rmi -f {}".format(rmImage))
		if output[0] == 0:
			success("Image {} removed successfully".format(rmImage))
				
	elif option == '10':
		container = input("\t\tEnter the Os name/id: ")
		
		output = sp.getstatusoutput("docker container ps -a")
		if container not in output[1]:
			success("OS not found")
		else:
			cloneName = input("\t\tSet name to new cloned Image: ")
			output = sp.getstatusoutput("docker commit {}  {}".format(container,cloneName))
			if output[0] == 0:
				success("Os {} cloned into {} Image successfully".format(container,cloneName))
		
	elif option == '11':
		output = sp.getstatusoutput("docker rm -f {}".format(input("\t\tEnter container name: ")))	
		if output[0] == 0:	
			success("container removed succesfully")
 
	elif option == '12':
		output = sp.getstatusoutput("docker rm -f  $(docker container ps -q -a)")
		print(output[1])	
		if output[0] == 0:
			success("All containers removed successfully")
	os.system("clear")
	return option
	


>>>>>>> 5c83bb767eaaebd4014652441b94d62496221d53
		
			
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
    text_menu();
else:
    r=sr.Recognizer()
    print("Please Speak!!!!!")
    with sr.Microphone() as source:
        a=sp.getoutput("clear")
    print(a)
    audio=r.listen(source)
    ins=r.recognize_google(audio)
    print(ins)
