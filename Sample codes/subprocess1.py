#Sample code for a python subprocess

import os
import subprocess
from subprocess import Popen


#s=subprocess.Popen("<cmd>",shell=True) 
      #Here, cmd can be any command you want to run in terminal as a subprocess
#out=s.communicate()

#python subprocess to kill all the terminal's
s=subprocess.Popen("sudo pkill terminal",shell=True)
out=s.communicate()

