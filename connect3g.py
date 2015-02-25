#!/usr/bin/env python
import subprocess
import re	
import time
import datetime

def getTime():
	return datetime.datetime.now()

def cmdRun(cmd):
	p = subprocess.Popen(cmd, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	p.wait();	
	out, err = p.communicate()
#	print out
	return out
	
def getConnect():
	print " Trwa laczenie"
	connectedStatus = cmdRun("/home/pi/Rpi3gConnector/connect3g.sh");
	cStatus = re.search("connected", connectedStatus)
	if cStatus:
		print " Polaczenie udane!"
	else:
		print " cos poszlo nie tak... sprobuje ponownie.."
		getConnect()

def checkHamachi():
	print " Check hamachi login"
	hamachiInfo = cmdRun("hamachi")
#	print hamachiInfo
	hamachiLoginStatus = re.search("logged in", hamachiInfo)

	return hamachiLoginStatus

def hamachiLogIn():
	print " Loguje do hamachi..."
	hamachiLoginAttempt = cmdRun("hamachi login")
	hamachiLoginStatus = re.search("(ok|logged in)", hamachiLoginAttempt)

	if hamachiLoginStatus:
		print " Zalogowano do hamachi"
	else:
		print " Jest problem z zalogowaniem do hamachi, ponowiam probe"
		hamachiLogIn()	
		

def checkConnection():
	print " Connection check... "
	pingResult = cmdRun("ping -c 1 wp.pl") 
	#pingLog = open("/home/pi/Rpi3gConnector/ping.log", "r").read()
#	print pingResult

	connectStatus = re.search("1 received", pingResult);

	return connectStatus


while (True):
	print getTime()

	connectStatus = checkConnection()

	if connectStatus:
		print "Polaczenie aktywne"
	else:
		print "Brak polaczenia... Polaczenie zostanie wznowione"
		getConnect()

	time.sleep(20)
	hamachiLoginStatus = checkHamachi()


	if hamachiLoginStatus:
		print "Zalogowany do hamachi"
	else:
		print "Brak zalogowania w hamachi. Zaloguje..."
		hamachiLogIn()


		







