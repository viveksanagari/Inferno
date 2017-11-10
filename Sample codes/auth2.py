from flask import Flask, request, make_response 
from functools import wraps

auth = Flask(__name__)

def auth_req(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		auth = request.authorization
		if auth and auth.username == 'vk' and auth.password == 'vk':
			return f(*args, **kwargs)
		return make_response('couldnt verify', 401, {'WWW-Authenticate' : 'Basic realm = "login required"'})
	return decorated

@auth.route('/')
@auth_req
def index():
	return 'This is the index page, which needs authorization to access\n'

if __name__ == '__main__':
	auth.run(debug=True)
