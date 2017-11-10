import os, sys
import subprocess
from subprocess import Popen
from Inferno_db import influx
from flask import Flask
from flask import request, Response, make_response
import threading
from threading import Thread

dpmi = Flask(__name__)

interface="wlp2s0"

directory="/home/vivek/consumer-bitrate"

global mainstream
mainstream=[]
global streams
streams=[]


def pkill():
	os.system('sudo pkill bitrate')
	return


def bitrate(str):
	os.chdir(directory)
	bitrate=subprocess.Popen(["unbuffer","./bitrate","-i",interface,str],stdout=subprocess.PIPE)
	influx_thread=threading.Thread(target=influx,args=(bitrate.stdout,str,)).start()
	
	
@dpmi.route('/startstream/<stream>', methods=['GET'])
def main(stream):
	global mainstream
	if not streams:
		if stream in mainstream:
				return '... bitrate stream %s is already running...\n' %stream
		else:
				streams.append(stream)
				mainstream=mainstream+streams
				bitrate_thread=threading.Thread(target=bitrate,args=(stream,)).start()
				bitrate_thread.deamon=True
				return '...bitrate stream  %s started...\n' %stream
	else:
		return '\n...a stream has already been started, use "addstream" to add...\n\n'

	
@dpmi.route('/showstream', methods=['GET'])
def show():
	if not mainstream: 
		return '...No streams available...\n'
	else:
		show=" ".join(str(S) for S in mainstream)
		return '...running bitrate streams %s...\n' %show

	
@dpmi.route('/addstream/<add>', methods=['GET'])
def add(add):
	global mainstream

	addstream=add.split(',')
	b=",".join(addstream)
	
	already=[]
	already=list(set(addstream).intersection(mainstream))
	stralready=" ".join(str(j) for j in already)
	
	new=[]
	new=list(set(addstream)-set(already))
	strnew=" ".join(str(i) for i in new)
	
	mainstream=mainstream+new
	
	for s in new:
		bitrate_add_thread=threading.Thread(target=bitrate,args=(s,)).start()
		bitrate_add_thread.deamon=True
	
	if not already:
		return '...adding bitrate streams %s...\n' %strnew
	else:
		return '...stream %s already running...\n...streams %s added...\n' %(stralready,strnew) 

	
@dpmi.route('/deletestream/<delet>', methods=['GET'])
def delete(delet):
	global mainstream
	
	delet=delet.split(',')

	suredel=[]
	suredel=list(set(delet).intersection(mainstream))
	strsuredel=" ".join(str(l) for l in suredel)
		
	cantdel=[]
	cantdel=list(set(delet)-set(suredel))
	strcantdel=" ".join(str(m) for m in cantdel)
	
	mainstream=list(set(mainstream)-set(suredel))
	strmainstream=",".join(str(k) for k in mainstream)

	if not suredel:
		return '...No streams available to delete...\n'
	else:
		pkill()
		for h in mainstream:
			bitrate_add_thread=threading.Thread(target=bitrate,args=(h,)).start() 
			bitrate_add_thread.deamon=True	
						
		if set(suredel).intersection(streams)!=0 :
			del streams[:]
			
		if not cantdel:		
			return "\n...bitrate stream %s deleted...\n\n" %(strsuredel)
		else:
			return "...bitrate stream %s deleted...\n...bitrate stream %s not available to delete...\n" %(strsuredel,strcantdel)
			
		
@dpmi.route('/changestream/<stream>', methods=['GET'])
def change(stream):

	global ch
	global mainstream

	ch=stream
	if ch in streams:
		return '\n...bitrate stream %s already running, change to another stream...\n\n' %ch
	else:
		stop()
		del streams[:]
		mainstream=list(set(mainstream)-set(streams))

		main(ch)
		return '\n...bitrate stream changed to %s...\n\n' %ch


@dpmi.route('/stop', methods=['GET'])
def stop():
	pkill()
	del (mainstream[:],streams[:])	
	return "...bitrate stream killed...\n"	


if __name__ == "__main__":
	dpmi.run(host='localhost', port=5000, debug=True)    
