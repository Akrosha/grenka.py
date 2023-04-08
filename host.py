from flask import Flask
from threading import Thread
from flask_restful import Api, Resource, reqparse
from helpers.databaseFunctions import check_user, just_get_all

app = Flask("")
api = Api(app)

@app.route("/", methods = ["get"])
def index():
    with open("webpages/index.html","r") as file:
        message = file.read()
    return message

@app.route("/home/", methods = ["get"])
def home():
    with open("webpages/home.html","r") as file:
        message = file.read()
    return message

@app.route("/help/", methods = ["get"])
def help():
    with open("webpages/help.html","r") as file:
        message = file.read()
    return message

@app.route("/api/user/", methods = ["get"])
def api_user():
    player = just_get_all()
    return {"status_code": 200, "data": player}

@app.route("/api/user/<string:uid>/", methods = ["get"])
def api_user_uid(uid: str):
    player = check_user(uid)
    if player:
        return {"status_code": 200, "data": player}
    else:
        return {"status_code": 404}

def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    tahread = Thread(target=run)
    tahread.start()