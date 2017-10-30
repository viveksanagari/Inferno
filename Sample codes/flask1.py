#This sample code assumes that Flask Python Module is already installed.

from flask import Flask
myapp = Flask(__name__)

@myapp.route("/")
def hi():
  return "hi \n"  

@myapp.route("/my")
def m():
  return "This is function 'm' for the route '/my' \n"  

myapp.run(host='localhost', port=5000, debug=True)    
