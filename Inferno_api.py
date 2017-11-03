import os, sys
import subprocess
from subprocess import Popen
from bitrate_db import influx
from flask import Flask
from flask import request, Response, make_response
import threading
from threading import Thread

app = Flask(__name__)

@app.route('/startstream/<stream>', methods=['GET'])

@app.route('/showstream', methods=['GET'])

@app.route('/addstream/<add>', methods=['GET'])

@app.route('/deletestream/<delet>', methods=['GET'])

@app.route('/changestream/<stream>', methods=['GET'])

@app.route('/stop', methods=['GET'])

if __name__ == "__main__":
	app.run(host='localhost', port=5000, debug=True)    
