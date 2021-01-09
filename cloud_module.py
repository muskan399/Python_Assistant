import os
import subprocess as sp
from hadoop_module import hadoop
from docker_module import docker
from greeting_module import close
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
    



def multi_cloud():
	
    os.system("clear")
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
            break
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

