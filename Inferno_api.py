import os, sys
import subprocess
from subprocess import Popen
from Inferno_db import influx
from flask import Flask
from flask import request, Response, make_response
import threading
from threading import Thread

app = Flask(__name__)

global mainstream
mainstream=[]
global streams
streams=[]


def bitrate(str):
	global stream
	stream=str
	os.chdir("/home/vivek/consumer-bitrate")
	bitrate=subprocess.Popen(["unbuffer","./bitrate","-i","wlp2s0.1",stream],stdout=subprocess.PIPE)
	influx_thread=threading.Thread(target=influx,args=(bitrate.stdout,)).start()
	
	
@app.route('/startstream/<stream>', methods=['GET'])
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
		return 'There is a stream already running, use another\n'

	
@app.route('/showstream', methods=['GET'])
def show():
	if not mainstream: 
		return '...No streams available...\n'
	else:
		show=" ".join(str(S) for S in mainstream)
		return '...running bitrate streams %s...\n' %show

	
@app.route('/addstream/<add>', methods=['GET'])
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

	
@app.route('/deletestream/<delet>', methods=['GET'])
def delete(delet):
	global mainstream
	
	delet=delet.split(',')

	suredel=[]
	suredel=list(set(delet).intersection(mainstream))

	cantdel=[]
	cantdel=list(set(delet)-set(suredel))
	
	if not cantdel:
		mainstream=list(set(mainstream)-set(suredel))
		strmainstream=",".join(str(k) for k in mainstream) # str of mainstream
	
		pkill()
		add(strmainstream)
		
		strsuredel=",".join(str(l) for l in suredel)

		if set(suredel).intersection(streams)!=0 :
			del streams[:]

		return "...bitrate stream %s deleted...\n" %(strsuredel)

	elif not suredel:
		return '...No streams available to delete...\n'	
		
	else:
		if set(suredel).intersection(streams)!=0 :
			del streams[:]
			
		return "...bitrate stream %s deleted...\n" %(strsuredel)
		
		
@app.route('/changestream/<stream>', methods=['GET'])
def change(stream):

	global ch
	global mainstream

	ch=stream
	if ch in streams:
		return 'change to another stream\n'		
	else:
		main(ch)
		return 'changed to %s\n' %ch


@app.route('/stop', methods=['GET'])
def stop():
	pkill()
	del (mainstream[:],streams[:])	
	return "...bitrate stream killed...\n"	


if __name__ == "__main__":
	app.run(host='localhost', port=5000, debug=True)    
