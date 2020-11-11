import speech_recognition as sr
import subprocess
import pyttsx3
import os


def close():
    subprocess.getoutput("pulseaudio --start")
    os.system("tput reset")
    os.system("espeak-ng 'Thank you'")
    print("Thank you for using my services!!")
    exit()

def text_menu():
    subprocess.getoutput("pulseaudio --start")
    os.system("tput setaf 2")
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
    elif option==4:
        close()

def multi_cloud():
    while(True):
        subprocess.getoutput("pulseaudio --start")
        print("\t\t\t\t\tMULTI CLOUD SERVICES")
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


def aws():
    while(True):
        subprocess.getoutput("pulseaudio --start")
        print("\t\t\t\t\tAMAZON WEB SERVICES")
        os.system("espeak-ng 'Use amazon web services'")
        print("""
1. Launch Ec2 instance
2. Create a S3 bucket
3. Launch a database server(RDS)
4. Create VPC network
5. Go back
6. Exit

    """)
        os.system("tput setaf 4")
        ch=int(input())
        os.system("clear")
        if(ch==1):
            os.system("espeak-ng 'Instance Launched'")
            print("Instance Launched!!!")
        elif(ch==2):
            os.system("espeak-ng 'S3 bucket created'")
            print("S3 bucker created!!")
        elif(ch==3):
            os.system("espeak-ng 'database server launched'")
            print("Database server launched!!")
        elif(ch==4):
            os.system("espeak-ng 'VPC created'")
            print("VPC created")
        elif(ch==5):
            multi_cloud()
        elif(ch==6):
            close()


def gcp():
    while(True):
        subprocess.getoutput("pulseaudio --start")
        print("\t\t\t\t\tGOOGLE CLOUD PLATFORM")
        os.system("espeak-ng 'Use Google Cloud Platform'")
        print("""
1. Launch Ec2 instance
2. Create a S3 bucket
3. Launch a database server(RDS)
4. Create VPC network
5. Go back
6. Exit
    """)
        os.system("tput setaf 4")
        ch=int(input())
        os.system("clear")
        if(ch==1):
            os.system("espeak-ng Instance Launched")
        elif(ch==2):
            os.system("espeak-ng S3 bucket created")
        elif(ch==3):
            os.system("espeak-ng database server launched")
        elif(ch==4):
            os.system("espeak-ng VPC created")
        elif(ch==5):
            multi_cloud()
        elif(ch==6):
            close()

os.system("tput setaf 4")
os.system("tput bold")
print("Welcome")
print("Please enter the choice for communication")
print("""
1. Text
2. Voice
      """)
ch=int(input())
os.system("clear")
while(True):
    subprocess.getoutput("pulseaudio --start")
    if(ch==1):
        text_menu();
    else:
        r=sr.Recognizer()
        print("Please Speak!!!!!")
        with sr.Microphone() as source:
            a=subprocess.getoutput("clear")
            print(a)
            audio=r.listen(source)
        ins=r.recognize_google(audio)
        print(ins)

