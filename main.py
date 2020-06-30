from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_www():
    msg = "Hello World! Welcome.\n" 
    msg = msg + "New feature." 
    return msg
