import json
import sqlite3
from .randomFunctions import trueRandom

class Database():
    def __init__(self, file: str = "database/database.db"):
        self.connect = sqlite3.connect(file)
        self.cursor = self.connect.cursor()
    
    def execute(self, query: str):
        result = self.cursor.execute(query).fetchall()
        self.connect.commit()
        return result

# докс: https://metanit.com/sql/sqlite/

database = Database()

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

def really_all():
    with open("database/db.json", "r") as file:
        players = json.load(file)
    return players

# delete = True: player = id
# else: player = {id: {playerdata}}
def update_players(player, delete = False):
    with open("database/db.json", "r") as file:
        players = json.load(file)
    if delete:
        players.pop(player, None)
    else:
        players.update(player)
    with open("database/db.json", "w") as file:
        json.dump(players, file)

# player = playerdata
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

# player = playerdata
def edit_nplayer(player):
    uid = player.get("id")
    if not uid:
        return "add <string:id>"
    else:
        nplayer = check_user(uid)
        if not nplayer:
            return "player with <string:id> not exist"
        else:
            nplayer.update(player)
            update_players({uid:nplayer})
            return "ok"

# player = id
def delete_nplayer(player):
    if not player:
        return "add <string:id>"
    else:
        nplayer = check_user(player)
        if not nplayer:
            return "player with <string:id> not exist"
        else:
            update_players(player, delete=True)
            return "ok"

def get_all_items():
    with open("database/inventory.json", "r") as file:
        items = json.load(file)
    return items

def get_all_species():
    with open("database/items.json", "r") as file:
        species = json.load(file)
    return species

def get_item(id):
    items = get_all_items()
    item = items.get(id)
    return item

# get species by item id
def get_item_species(id):
    species = get_all_species()
    item = get_item(id)
    item_species = species.get(item.get("species"))
    return item_species

def get_species(species):
    allspecies = get_all_species()
    species = allspecies.get(species)
    return species

def get_player_inv(id):
    items = get_all_items()
    items = {key:items[key] for key in items if items[key]["owner_id"]==id}
    
    # [i for i in range(10) if i > 5]
    # [6, 7, 8, 9]
    
    # {key:a[key] for key in a if a[key]["owner"]=="akro"}
    # {'id1': {'owner': 'akro'}, 'id3': {'owner': 'akro'}}
    
    return items

# код редактирования предметов
# соответствует коду редактирования
# игроков, а все потому что их базы данных
# созданы по одной структуре:
# {id1: {data1}, id2: {data2}}
# можно было бы как-то переделать эти
# методы, чтобы сделать их универсальными
# для обоих баз, но тогда в другом коде
# всего бота придется менять входные
# аргументы для правильной работы
# :bread::cry:

# delete = True: item = id
# else: item = {id: {itemdata}}
def update_items(item, delete = False):
    with open("database/inventory.json", "r") as file:
        items = json.load(file)
    if delete:
        items.pop(item, None)
    else:
        items.update(item)
    with open("database/inventory.json", "w") as file:
        json.dump(items, file)

# item = itemdata
def add_nitem(item):
    uid = item.get("item_id")
    if not uid:
        return "add <string:id>"
    else:
        exist = get_item(uid)
        if exist:
            return "item with <string:id> exist"
        else:
            update_items({uid:item})
            return "ok"

# item = itemdata
def edit_nitem(item):
    uid = item.get("item_id")
    if not uid:
        return "add <string:id>"
    else:
        nitem = get_item(uid)
        if not nitem:
            return "item with <string:id> not exist"
        else:
            nitem.update(item)
            update_items({uid:nitem})
            return "ok"

# item = id
def delete_nitem(item):
    if not item:
        return "add <string:id>"
    else:
        nitem = get_item(item)
        if not nitem:
            return "item with <string:id> not exist"
        else:
            update_items(item, delete=True)
            return "ok"

def update_shop():
    species = list(get_all_species().values())
    shop = {}
    for i in range(int(trueRandom(1, 10))):
        item = species[int(trueRandom(0, len(species) - 1))]
        cost = item.get("cost") + int(trueRandom(0, item.get("cost")))
        shop.update(
            {
                str(i+1): {
                    "item": item.get("species"),
                    "price": cost
                }
            }
        )
    with open("database/shop.json", "w") as file:
        json.dump(shop, file)

def get_all_locations():
    with open("database/locations.json", "r") as file:
        locations = json.load(file)
    return locations

def get_location(id):
    locations = get_all_locations()
    location = locations.get(id, "void")
    return location