from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_www():
    return "Minor change. Hello World Wide Web!"
