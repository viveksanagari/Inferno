#Sample code to provide password automatically

import os, sys

def kill():
	sudo_Password = 'dragon'    #your password 
	command = 'sudo pkill chrome'
	kill = os.system('echo %s|sudo -S %s' % (sudo_Password, command))
	return

kill()
