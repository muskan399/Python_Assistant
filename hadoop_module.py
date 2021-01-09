import os
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
        return inp

       


