#Sample code to pipe output of python subprocess

import os
import subprocess
from subprocess import Popen

i = subprocess.Popen('ifconfig',stdout=subprocess.PIPE)
m = subprocess.Popen('grep inet',stdin=i.stdout,stdout=subprocess.PIPE,shell=True)
n = subprocess.Popen('grep 127.0.0.1',stdin=m.stdout,shell=True)
out=n.communicate()
