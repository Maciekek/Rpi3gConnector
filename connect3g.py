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

cmdRun("/home/pi/Rpi3gConnector/ping.sh")
pingLog = open("/home/pi/Rpi3gConnector/ping.log", "r").read()

connectStatus = re.search("1 received", pingLog);
#print pingLog
#print connectStatus.group()

while (True):
	getConnect()
	time.sleep(300)

		







