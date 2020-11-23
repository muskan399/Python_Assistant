import subprocess as sp
import pyttsx3
import os
import pyfiglet


#launch os function
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
	


		
			


def hadoop():
    print("------------Welcome to APACHE HADOOP SERVICES------------")
    print("----You are the Client----")
    while True:
        os.system("clear")
        print("""\n
        1. Setup Hadoop Cluster
        2. Get details of all slaves
        3. List all files in hadoop cluster
        4. Upload a file
        5. Read a file
        6. Remove a file
        7. Back to main menu
        8. Exit
        """)
        inp = int(input("Enter your choice: "))
        if inp == 7:
            text_menu()
        elif inp == 8:
            close()

        os.system("ssh-keygen")
        if inp == 1:

            #Configuring Master
            ip_master = input("Enter ip of master ")
            os.system("ssh-copy-id -i /root/.ssh/id_rsa.pub {}".format(ip_master))
            os.system("scp jdk-8u171-linux-x64.rpm {}:/".format(ip_master))
            os.system("scp hadoop-1.2.1-1.x86_64.rpm {}:/".format(ip_master))
            os.system("ssh {} rpm -i /jdk-8u171-linux-x64.rpm".format(ip_master))
            os.system("ssh {} rpm -i /hadoop-1.2.1-1.x86_64.rpm --force".format(ip_master))
            os.system("ssh {} mkdir /nn".format(ip_master))
            os.system("ssh {} echo -e \"`sed -i '$d' /etc/hadoop/hdfs-site.xml`<property>\n<name>dfs.name.dir</name>\n<value>/nn</value>\n</property>\n</configuration>\" >> /etc/hadoop/hdfs-site.xml".format(ip_master))
            os.system("ssh {} echo -e \"`sed -i '$d' /etc/hadoop/core-site.xml`<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n</configuration>\" >> /etc/hadoop/core-site.xml".format(ip_master,ip_master))
            os.system("ssh {} hadoop namenode -format".format(ip_master))
            os.system("ssh {} hadoop-daemon start namenode".format(ip_master))
            os.system("ssh {} systemctl stop firewalld".format(ip_master))

            #Configuring Slaves          
            no_of_slaves = int(input("Enter how many slaves you want ?"))
            for i in range(1,no_of_slaves+1):
                ip_slave = input("Enter ip of slave ")
                os.system("ssh-copy-id -i /root/.ssh/id_rsa.pub {}".format(ip_slave))
                os.system("scp jdk-8u171-linux-x64.rpm {}:/".format(ip_slave))
                os.system("scp hadoop-1.2.1-1.x86_64.rpm {}:/".format(ip_slave))
                os.system("ssh {} rpm -i /jdk-8u171-linux-x64.rpm".format(ip_slave))
                os.system("ssh {} rpm -i /hadoop-1.2.1-1.x86_64.rpm --force".format(ip_slave))
                os.system("ssh {} mkdir /dn{}".format(ip_slave,i))
                os.system("ssh {} echo -e \"`sed -i '$d' /etc/hadoop/hdfs-site.xml`<property>\n<name>dfs.data.dir</name>\n<value>/dn{}</value>\n</property>\n</configuration>\" >> /etc/hadoop/hdfs-site.xml".format(ip_slave,i))
                os.system("ssh {} echo -e \"`sed -i '$d' /etc/hadoop/core-site.xml`<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n</configuration>\" >> /etc/hadoop/core-site.xml".format(ip_slave,ip_master))
                os.system("ssh {} hadoop-daemon start datanode".format(ip_slave))

            #Configuring Client
            os.system("rpm -i jdk-8u171-linux-x64.rpm")
            os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm")
            os.system("echo -e \"`sed -i '$d' /etc/hadoop/core-site.xml`<property>\n<name>fs.default.name</name>\n<value>hdfs://{}:9001</value>\n</property>\n</configuration>\" >> /etc/hadoop/core-site.xml".format(ip_master))                          

        elif inp == 2:
            os.system("hadoop dfsadmin -report")

        elif inp == 3:
            os.system("hadoop fs -ls  /")

        elif inp == 4:
            filename = input("Enter filename")
            os.system("hadoop fs -put {} /".format(filename))

        elif inp == 5:
            filename = input("Enter filename")
            os.system("hadoop fs -cat {} /".format(filename))

        elif inp == 6:
            filename = input("Enter filename")
            os.system("hadoop fs -rm {} /".format(filename))
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
4. Exit
    """)
    os.system("tput setaf 6")
    option=int(input())
    os.system("clear")
    if option==1:
        multi_cloud()
    elif option==2:
        while(1):
            o=docker()
            if o=='13':
                text_menu()
                break
            elif o=='14':
                close()
                break
            
    elif option==3:
        hadoop()
    elif option==4:
        close()
    

def multi_cloud():
    os.system("clear")
    while(True):
        sp.getoutput("pulseaudio --start")
        os.system("figlet 'Multi-Cloud Services'")
        os.system("espeak-ng 'We are providing Multi Cloud services'")
        print("""
1. Amazon Web Services(AWS)
2. Google Cloud Platform(GCP)
3. Go back
4. Exit
    """)
        os.system("tput setaf 3")
        cloud_choice=int(input())
        os.system("clear")
        if(cloud_choice==1):
            aws()
        elif(cloud_choice==2):
            gcp()
        elif(cloud_choice==3):
            text_menu()
        elif(cloud_choice==4):
            close()
        os.system("clear")


def aws():

    while(True):
        sp.getoutput("pulseaudio --start")
        os.system("figlet '                          AWS'")
        os.system("espeak-ng 'Use amazon web services'")
        print("""
1. Launch Ec2 instance
2. List all the instances
3. Stop an instance
4. Start an instance
5. Terminate a instance
6. Create a S3 bucket
7. List all the buckets
8. Sync bucket with a local directory
9. Go back
10.Exit
    """)
        os.system("tput setaf 4")
        ch=int(input())
        os.system("clear")

        if(ch==1):
            os.system("figlet Details\n")
            print("\n\nEnter the details!!\n")
            os.system("espeak-ng 'Enter the details'")
            print("\nOS name")
            os.system("espeak-ng 'Enter the OS name'")
            os_name=input()
            x=sp.getstatusoutput("aws ec2 run-instances --image-id ami-026669ec456129a70 --count 1 --instance-type t2.micro --key-name os_key --security-groups default")
            
            if(x[0]==0):
                print('\nInstance Launched!!!\n')
                os.system("espeak-ng 'Instance launched please check your AWS account'")
            else:
                print("\nSomething went wrong!!")
            os.system("clear")
	    
        elif(ch==2):
            os.system('aws ec2 describe-instances --query "Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[0].Value,State:State.Name}" --output text')
            print("\n\nPress 1 to go back")
            e=input()
            if(e==1):
            	multi_cloud()
        elif(ch==3):
            os.system("figlet Details")
            os.system("espeak-ng 'Stop an instance")
            os.system("figlet Details\n")
            print("\n\nEnter the details!!\n")
            os.system("espeak-ng 'Enter the details'")
            print("\nOS name")
            os.system("espeak-ng 'Enter the instance id'")
            os.system('aws ec2 describe-instances --query "Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[0].Value,State:State.Name}" --output text')
            ins_id=input()
            x=sp.getoutput("aws ec2 stop-instances --instance-id {0}".format(ins_id))
            if(x[0]==0):
                print("\nInstance Stopped!!!\n")
                os.system("espeak-ng 'Instance stopped please check your AWS account'")
            else:
                print("\nSomething went wrong!!")
            os.system("clear")
        elif(ch==4):
            os.system("figlet Details")
            os.system("espeak-ng 'Start an instance")
            os.system("figlet Details\n")
            print("\n\nEnter the details!!\n")
            os.system("espeak-ng 'Enter the details'")
            print("\nOS name")
            os.system("espeak-ng 'Enter the instance id'")
            os.system('aws ec2 describe-instances --query "Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[0].Value,State:State.Name}" --output text')
            ins_id=input()
            x=sp.getoutput("aws ec2 start-instances --instance-id {0}".format(ins_id))
            if(x[0]==0):
                print("\nInstance Started!!!\n")
                os.system("espeak-ng 'Instance started please check your AWS account'")
            else:
                print("\nSomething went wrong!!")
            os.system("clear")
        elif(ch==5):
            os.system("figlet Details")
            os.system("espeak-ng 'Terminate an instance")
            os.system("figlet Details\n")
            print("\n\nEnter the details!!\n")
            os.system("espeak-ng 'Enter the details'")
            print("\nOS name")
            os.system("espeak-ng 'Enter the instance id'")
            os.system('aws ec2 describe-instances --query "Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[0].Value,State:State.Name}" --output text')
            ins_id=input()
            x=sp.getstatusoutput("aws ec2 terminate-instances --instance-id {0}".format(ins_id))
            if(x[0]==0):
                print("\nInstance Terminated!!!\n")
                os.system("espeak-ng 'Instance terminated please check your AWS account'")
            else:
                print("\nSomething went wrong!!")
            os.system("clear")
        elif(ch==6):
            os.system("figlet Details\n")
            print("\n\nEnter the details!!\n")
            os.system("espeak-ng 'Enter the details'")
            print("\nEnter the bucket name")
            os.system("espeak-ng 'Enter the Bucket name(Should be unique in a region'")
            os_name=input()
            x=sp.getoutput('aws s3api create-bucket --bucket bucket9425 --create-bucket-configuration LocationConstraint=ap-south-1 --query {"Location:Location"} --output text')
            if(x[0]==0):
                print("\nBucket created!!!\n")
                os.system("espeak-ng 'Bucket created please check your AWS account'")
            else:
                print("\nSomething went wrong!!")
            os.system("clear")
        elif(ch==7):
            os.system("aws s3api list-buckets --query 'Buckets[*].{Name:Name,CreationDate: CreationDate}' --output text")
            print("\n\nPress 1 to go back")
            e=input()
            if(e==1):
                multi_cloud()
        elif(ch==8):
            os.system("figlet Details\n")
            print("\n\nEnter the details!!\n")
            os.system("espeak-ng 'Enter the details'")
            print("\nEnter the directory path")
            os.system("espeak-ng 'Enter the Directory path'")
            dir_path=input()
            print("\nBucket name")
            os.system("aws s3api list-buckets --query 'Buckets[*].{Name:Name,CreationDate: CreationDate}' --output text")
            os.system("espeak-ng 'Enter the Bucket name'")
            buc_name=input()
            x=sp.getstatusoutput("aws s3 sync {0} s3://{1}".format(dir_path,buc_name))
            if(x[0]==0):
              print("\nBucket synced!!!\n")
              os.system("espeak-ng 'Bucket synced please check your AWS account'")
            else:
                print("\nSomething went wrong!!")
            os.system("clear")
           
        elif(ch==9):
            multi_cloud()
        elif(ch==10):
            close()
            break
        os.system("clear")


def gcp():
    while(True):
        sp.getoutput("pulseaudio --start")
        os.system("figlet '                          GCP'")
        os.system("espeak-ng 'Use Google Cloud Platform'")
        print("""
*****Work in Progress***
1. Go back
2.  Exit
    """)
        o=int(input())
        if o==1:
           multi_cloud()
        else:
           close()
    os.system("clear")
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
while(True):
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
