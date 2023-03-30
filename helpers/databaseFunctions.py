import json

def check_user(player_id: str):
    with open("database/db.json", "r") as file:
        players = json.load(file)
    if player_id in players:
        return players[player_id]
    else:
        return None

def update_players(player):
    with open("database/db.json", "r") as file:
        players = json.load(file)
    players.update(player)
    with open("database/db.json", "w") as file:
        json.dump(players, file)