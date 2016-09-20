from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return '''<h1>Welcome to Misha's homepage!</h1><br>
		Go to:<br>
		<a href="/about">About</a><br>
		<a href="/revolution">Revolution</a>
		'''

@app.route("/about")
def about():
	return '''<h1>About</h1><br>
		This is a test Flask app made by Misha<br>
		<br>
		Go to:<br>
		<a href="/">Home</a><br>
		<a href="/revolution">Revolution</a>
		'''

@app.route("/revolution")
def revolution():
	return '''<h1>Revolution</h1><br>
		Click <a href="https://www.youtube.com/watch?v=w8KQmps-Sog">here</a> for a cool video from MUSE<br>
		<br>
		Go to:<br>
		<a href="/">Home</a><br>
		<a href="/about">About</a>
		'''


app.run()
