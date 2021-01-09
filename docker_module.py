import os
import subprocess as sp
import pyfiglet
from greeting_module import close



def launchOs():
	image = input("\n\t\tType the image name with version(like, unbuntu:14.04): ")
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
	elif option == '13':
		return
	elif option == '14':
		close()
	os.system("clear")
	return option
	
