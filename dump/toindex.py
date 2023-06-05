import os
import json
from flask import Flask, request
from threading import Thread

app = Flask("")

@app.route("/", methods = ["get"])
def index():
    with open("index.html","r") as file:
        message = file.read()
    return message, 200

def run():
    app.run(host="127.0.0.1", port=8080)


def keep_alive():
    tahread = Thread(target=run)
    tahread.start()
