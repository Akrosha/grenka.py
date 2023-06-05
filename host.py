import os
import json
from threading import Thread
from flask import Flask, request
from helpers.databaseFunctions import check_user, just_get_all, add_nplayer, edit_nplayer, delete_nplayer
from helpers.randomFunctions import logger

app = Flask("")

@app.route("/", methods = ["get"])
def index():
    with open("static/index.html", "r") as file:
        message = file.read()
    logger("checked")
    return message, 200

@app.route("/api/user/", methods = ["GET", "POST", "PUT", "DELETE"])
def api_user():
    try:
        dataf = json.loads(request.data.decode("utf-8"))
    except:
        dataf = {}
    if request.method == "GET":
        player = just_get_all()
        return {"status_code": 200, "data": player}, 200
    elif request.method == "POST":
        if dataf.get("api_key", "password") != os.getenv("api_key"):
            return {"status_code": 401}, 401
        else:
            dataf.pop("api_key", None)
            add_nplayer(dataf)
            return {"status_code": 200}, 200
    elif request.method == "PUT":
        if dataf.get("api_key", "password") != os.getenv("api_key"):
            return {"status_code": 401}, 401
        else:
            dataf.pop("api_key", None)
            edit_nplayer(dataf)
            return {"status_code": 200}, 200
    elif request.method == "DELETE":
        if dataf.get("api_key", "password") != os.getenv("api_key"):
            return {"status_code": 401}, 401
        else:
            dataf.pop("api_key", None)
            delete_nplayer(dataf)
            return {"status_code": 200}, 200

@app.route("/api/user/<string:uid>/", methods = ["GET"])
def api_user_uid(uid: str):
    player = check_user(uid)
    if player:
        return {"status_code": 200, "data": player}, 200
    else:
        return {"status_code": 404}, 404

@app.route('/killthisdashitsuka/', methods=['GET'])
def killthisdashitsuka():
    try:
        dataf = json.loads(request.data.decode("utf-8"))
    except:
        dataf = {}
    if dataf.get("api_key", "password") != os.getenv("api_key"):
        return {"status_code": 401}, 401
    else:
        #os.kill(os.getpid(), signal.SIGINT)
        raise SystemExit
        return "fuck you"

def runapp():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    tahread = Thread(target=runapp)
    tahread.start()