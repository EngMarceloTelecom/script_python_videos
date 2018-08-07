#!/usr/bin/python
import getpass
import sys
import telnetlib

user = raw_input("Digite seu usuario Telnet: ")
password = getpass.getpass()

for i in range (11,16):
    HOST = "192.168.126."+str(i)


    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")


    tn.write("\n")
    tn.write("conf t\n")

    for i in range (10,110,10):
        tn.write("no vlan " + str(i) + "\n" )
        tn.write("name DevNetPython_" + str(i) + "\n" )

    tn.write("end\n")
    tn.write("exit\n")

    print tn.read_all()
