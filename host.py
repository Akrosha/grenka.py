from flask import Flask
from threading import Thread

app = Flask("")


@app.route('/')
def index():
    with open("webpages/index.html","r") as file:
        message = file.read()
    return message

@app.route('/home/')
def home():
    with open("webpages/home.html","r") as file:
        message = file.read()
    return message

@app.route("/help/")
def help():
    with open("webpages/help.html","r") as file:
        message = file.read()
    return message


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    tahread = Thread(target=run)
    tahread.start()