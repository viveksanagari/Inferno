#This sample code assumes that Flask Python Module is already installed.

from flask import Flask
myapp = Flask(__name__)

#Input to the flask 'myapp' application with a variable 'dragon'
@myapp.route('/<dragon>')
def a(dragon):

      #perform any required processing with the input of this '/' route in this function, using 'dragon' variable.

  return "The input for this function is %s" %dragon  

@myapp.route('/new/<next>')
def b(next):

      #perform any required processing with the input of this '/new' route in this function, using 'next' variable.

  return "The input for this function is %s" %next  

myapp.run(host='localhost', port=5000, debug=True) 
