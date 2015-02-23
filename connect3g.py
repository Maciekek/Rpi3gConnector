#!/usr/bin/env python
import subprocess
import re	
import time

def cmdRun(cmd):
	p = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	p.wait();	
	out, err = p.communicate()
	print out
	return out
	
def getConnect():
	print "Trwa laczenie"
	connectedStatus = cmdRun("/home/pi/Rpi3gConnector/connect3g.sh");
	cStatus = re.search("connected", connectedStatus)
	if cStatus:
		print "Polaczenie udane!"
	else:
		print "cos poszlo nie tak... sprobuje ponownie.."
		getConnect()
	
	

print "Hi"
print "Ping run"

def checkConnection():
	print "Connection check... "
	pingResult = cmdRun("ping -c 1 wp.pl > ping.log") 
	#pingLog = open("/home/pi/Rpi3gConnector/ping.log", "r").read()
	print pingResult
	connectStatus = re.search("1 received", pingResult);
	#print pingLog
	#print connectStatus.group()
	return connectStatus

while (True):
	connectStatus = checkConnection()
	if connectStatus:
		print "Polaczenie aktywne"
	else:
		print "Brak polaczenia... Polaczenie zostanie wznowione"
		getConnect()
	
	time.sleep(20)

		







