from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Welcome to Misha's homepage!"

@app.route("/about")
def about():
	return "This is a test Flask app made by Misha"

@app.route("/revolution")
def revolution():
	return 'Click <a href="https://www.youtuve.com/watch?v=w8KQmps-Sog">here</a> for a cool video from MUSE'

app.run()
