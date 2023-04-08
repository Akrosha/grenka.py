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

def update_players(player):
    with open("database/db.json", "r") as file:
        players = json.load(file)
    players.update(player)
    with open("database/db.json", "w") as file:
        json.dump(players, file)