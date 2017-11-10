from flask import Flask, request, make_response 
from functools import wraps

app = Flask(__name__)

def auth_req():
    # something to verify authorization 
    

@app.route('/')
@auth_req
def mainpage():
	return 'you are on the main page'


if __name__ == '__main__':
	app.run(debug=True)
