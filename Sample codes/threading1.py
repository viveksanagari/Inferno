#Sample code to use Threading with functions

import threading
from threading import Thread

x=[]
y=[]
m=10

def append1(m):
	append2_thread = threading.Thread(target=append2,args=(m,)).start()
	for a in range (m):
		global x
		x.append(a)
	print "x=",x	
		
def append2(m):
	for b in range(m):
		y.append(b+m)
	print "y=",y
	
append1_thread = threading.Thread(target=append1,args=(m,)).start()
