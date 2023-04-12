import json

def check_user(player_id: str):
    with open("database/db.json", "r") as file:
        players = json.load(file)
    if player_id in players:
        return players[player_id]
    else:
        return None

def just_get_all(page:int = 1, step:int = 5):
    with open("database/db.json", "r") as file:
        players = json.load(file)
        keys = list(players.keys())[step*(page-1):step*page]
        players = {key:players[key] for key in keys}
    return players

# delete = True: player = id
# else: player = {id: player}
def update_players(player, delete = False):
    with open("database/db.json", "r") as file:
        players = json.load(file)
    if delete:
        players.pop(player, None)
    else:
        players.update(player)
    with open("database/db.json", "w") as file:
        json.dump(players, file)

def add_nplayer(player):
    uid = player.get("id")
    if not uid:
        return "add <string:id>"
    else:
        exist = check_user(uid)
        if exist:
            return "player with <string:id> exist"
        else:
            update_players({uid:player})
            return "ok"

def edit_nplayer(player):
    uid = player.get("id")
    if not uid:
        return "add <string:id>"
    else:
        nplayer = check_user(uid)
        if not player:
            return "player with <string:id> not exist"
        else:
            nplayer.update(player)
            update_players({uid:nplayer})
            return "ok"

def delete_nplayer(player):
    uid = player.get("id")
    if not uid:
        return "add <string:id>"
    else:
        nplayer = check_user(uid)
        if not player:
            return "player with <string:id> not exist"
        else:
            update_players(uid, delete=True)
            return "ok"
