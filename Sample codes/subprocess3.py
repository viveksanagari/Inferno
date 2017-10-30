#Sample code to process the piped output of python subprocess

  #type 'ifconfig' in the terminal, also try this code and view the difference.

import os
import subprocess
from subprocess import Popen

i = subprocess.Popen('ifconfig',stdout=subprocess.PIPE)
m = subprocess.Popen('grep inet6',stdin=i.stdout,stdout=subprocess.PIPE,shell=True)

for n in iter(m.stdout.readline,''):
	l=n.rstrip()
	line_split=l.split()
	a=line_split[0]
	b=line_split[1]
	c=line_split[2]
	d=line_split[3]
	print a,"|",b,"|",c,"|",d
