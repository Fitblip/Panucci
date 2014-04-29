from flask import Flask, render_template
app = Flask(__name__)

import boto
import cloudwatch
import config

@app.route("/info.json")
def hello():
	return cloudwatch.getStuff()

@app.route('/')
def blah():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
