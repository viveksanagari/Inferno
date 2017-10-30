#This sample code assumes that Flask Python Module is already installed.

from flask import Flask
myapp = Flask(__name__)

@myapp.route("/")
def hi():
  return "hi"  
  
myapp.run(host='localhost', port=5000, debug=True)    
