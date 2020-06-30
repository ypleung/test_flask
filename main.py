from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_www():
    msg = "Hello World! Welcome." 
    msg = msg + "\n" + "Adding some features."
    return msg
