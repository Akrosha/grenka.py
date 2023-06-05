import json
import sqlite3
from .randomFunctions import trueRandom

# надо для sql запросов
def var_type(var):
    if isinstance(var, bool):
        return f"{int(var)}"
    elif isinstance(var, (int, float)):
        return f"{var}"
    elif isinstance(var, str):
        return f"'{var}'"
    elif isinstance(var, (dict, list)):
        return f"{json.dumps(var)}"

class Database():
    def __init__(self, file: str = "database/database.db"):
        self.file = file
        self.connect = sqlite3.connect(self.file)
        self.cursor = self.connect.cursor()
    
    def dbreload(self):
        self.connect.commit()
        self.connect.close()
        self.connect = sqlite3.connect(self.file)
        self.cursor = self.connect.cursor()
    
    def execute(self, query: str, fetchall: bool = False):
        try:
            if fetchall:
                result = self.cursor.execute(query).fetchall()
            else:
                result = self.cursor.execute(query).fetchone()
            self.connect.commit()
        except:
            result = None
        return result

# докс: https://metanit.com/sql/sqlite/

database = Database()

def check_user(player_id: str = "Nan", name: str = "NaN"):
    player_id = database.execute(f"SELECT id FROM users WHERE id = '{player_id}' OR name = '{name}'")
    if player_id:
        player = {}
        columns = database.execute(f"pragma table_info(users)", fetchall = True)
        for column in columns:
            info = database.execute(f"SELECT {column[1]} FROM users WHERE id = '{player_id[0]}'")
            if column[2] == "BLOB":
                info = json.loads(info[0])
            else:
                info = info[0]
            player.update({column[1]: info})
        return player
    else:
        return None

def just_get_all(page: int = 1, step: int = 5):
    players = {}
    player_ids = database.execute(f"SELECT id FROM users LIMIT {(page - 1)*step}, {step}", fetchall = True)
    for player_id in player_ids:
        player = {}
        columns = database.execute(f"pragma table_info(users)", fetchall = True)
        for column in columns:
            info = database.execute(f"SELECT {column[1]} FROM users WHERE id = '{player_id[0]}'")
            if column[2] == "BLOB":
                info = json.loads(info[0])
            else:
                info = info[0]
            player.update({column[1]: info})
        players.update({player_id[0]:player})
    return players

def really_all():
    players = {}
    player_ids = database.execute(f"SELECT id FROM users", fetchall = True)
    for player_id in player_ids:
        player = {}
        columns = database.execute(f"pragma table_info(users)", fetchall = True)
        for column in columns:
            info = database.execute(f"SELECT {column[1]} FROM users WHERE id = '{player_id[0]}'")
            if column[2] == "BLOB":
                info = json.loads(info[0])
            else:
                info = info[0]
            player.update({column[1]: info})
        players.update({player_id[0]:player})
    return players

# no needs
"""
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
"""

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
            keys = ", ".join([key for key in player.keys()])
            values = ", ".join([var_type(value) for value in player.values()])
            database.execute(f"INSERT INTO users ({keys}) VALUES ({values})")
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
            keys = " = {}, ".join([key for key in nplayer.keys()]) + " = {}"
            values = [var_type(value) for value in nplayer.values()]
            database.execute(f"UPDATE users SET {keys.format(*values)} WHERE id = '{uid}'")
            return "ok"

# delete player by id
def delete_nplayer(uid):
    if not uid:
        return "add <string:id>"
    else:
        nplayer = check_user(uid)
        if not nplayer:
            return "player with <string:id> not exist"
        else:
            database.execute(f"DELETE FROM users WHERE id = '{uid}'")
            return "ok"

# no needs
"""
def get_all_items():
    with open("database/inventory.json", "r") as file:
        items = json.load(file)
    return items

def get_all_species():
    with open("database/items.json", "r") as file:
        species = json.load(file)
    return species
"""

def get_item(item_id):
    item_id = database.execute(f"SELECT item_id FROM inventory WHERE item_id = '{item_id}'")
    if item_id:
        item = {}
        columns = database.execute(f"pragma table_info(inventory)", fetchall = True)
        for column in columns:
            info = database.execute(f"SELECT {column[1]} FROM inventory WHERE item_id = '{item_id[0]}'")
            if column[2] == "BLOB":
                info = json.loads(info[0])
            else:
                info = info[0]
            item.update({column[1]: info})
        return item
    else:
        return None

# get species by item id
def get_item_species(item_id):
    species_id = database.execute(f"SELECT species FROM inventory WHERE item_id = '{item_id}'")
    if species_id:
        species = {}
        columns = database.execute(f"pragma table_info(items)", fetchall = True)
        for column in columns:
            info = database.execute(f"SELECT {column[1]} FROM items WHERE species = '{species_id[0]}'")
            if column[2] == "BLOB":
                info = json.loads(info[0])
            else:
                info = info[0]
            species.update({column[1]: info})
        return species
    else:
        return None

def get_species(species_id):
    species_id = database.execute(f"SELECT species FROM items WHERE species = '{species_id}'")
    if species_id:
        species = {}
        columns = database.execute(f"pragma table_info(items)", fetchall = True)
        for column in columns:
            info = database.execute(f"SELECT {column[1]} FROM items WHERE species = '{species_id[0]}'")
            if column[2] == "BLOB":
                info = json.loads(info[0])
            else:
                info = info[0]
            species.update({column[1]: info})
        return species
    else:
        return None

def get_player_inv(player_id):
    items = {}
    item_ids = database.execute(f"SELECT item_id FROM inventory WHERE owner_id = '{player_id}'", fetchall = True)
    for item_id in item_ids:
        item = {}
        columns = database.execute(f"pragma table_info(inventory)", fetchall = True)
        for column in columns:
            info = database.execute(f"SELECT {column[1]} FROM inventory WHERE item_id = '{item_id[0]}'")
            if column[2] == "BLOB":
                info = json.loads(info[0])
            else:
                info = info[0]
            item.update({column[1]: info})
        items.update({item_id[0]:item})
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

# no needs
"""
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
"""

# item = itemdata
def add_nitem(item):
    item_id = item.get("item_id")
    if not item_id:
        return "add <string:id>"
    else:
        exist = get_item(item_id)
        if exist:
            return "item with <string:id> exist"
        else:
            keys = ", ".join([key for key in item.keys()])
            values = ", ".join([var_type(value) for value in item.values()])
            database.execute(f"INSERT INTO inventory ({keys}) VALUES ({values})")
            return "ok"

# item = itemdata
def edit_nitem(item):
    item_id = item.get("item_id")
    if not item_id:
        return "add <string:id>"
    else:
        nitem = get_item(item_id)
        if not nitem:
            return "item with <string:id> not exist"
        else:
            nitem.update(item)
            keys = " = {}, ".join([key for key in nitem.keys()]) + " = {}"
            values = [var_type(value) for value in nitem.values()]
            database.execute(f"UPDATE inventory SET {keys.format(*values)} WHERE item_id = '{item_id}'")
            return "ok"

# delete item by id
def delete_nitem(item_id):
    if not item_id:
        return "add <string:id>"
    else:
        nitem = get_item(item_id)
        if not nitem:
            return "item with <string:id> not exist"
        else:
            database.execute(f"DELETE FROM inventory WHERE item_id = '{item_id}'")
            return "ok"

def get_shop():
    shop = {}
    shop_ids = database.execute(f"SELECT id FROM shop", fetchall = True)
    for shop_id in shop_ids:
        item = {}
        columns = database.execute(f"pragma table_info(shop)", fetchall = True)
        for column in columns:
            info = database.execute(f"SELECT {column[1]} FROM shop WHERE id = '{shop_id[0]}'")
            if column[2] == "BLOB":
                info = json.loads(info[0])
            else:
                info = info[0]
            item.update({column[1]: info})
        shop.update({shop_id[0]:item})
    return shop

def update_shop():
    database.execute(f"DELETE FROM shop")
    
    species = database.execute(f"SELECT species, cost FROM items", fetchall = True)
    
    for i in range(int(trueRandom(1, 10))):
        item = species[int(trueRandom(0, len(species) - 1))]
        cost = item[1] + int(trueRandom(0, item[1]))
        database.execute(f"INSERT INTO shop (id, item, price) VALUES ('{str(i+1)}', '{item[0]}', '{cost}')")

# no needs
"""
def get_all_locations():
    with open("database/locations.json", "r") as file:
        locations = json.load(file)
    return locations
"""

def get_location(loc_id):
    loc_id = database.execute(f"SELECT loc_id FROM locations WHERE loc_id = '{loc_id}'")
    if loc_id:
        loc_id = loc_id[0]
    else:
        loc_id = "void"
    
    location = {}
    columns = database.execute(f"pragma table_info(locations)", fetchall = True)
    for column in columns:
        info = database.execute(f"SELECT {column[1]} FROM locations WHERE loc_id = '{loc_id}'")
        if column[2] == "BLOB":
            info = json.loads(info[0])
        else:
            info = info[0]
        location.update({column[1]: info})
    return location

def get_ideas():
    ideas = {}
    idea_ids = database.execute(f"SELECT id FROM ideas", fetchall = True)
    for idea_id in idea_ids:
        idea = {}
        columns = database.execute(f"pragma table_info(ideas)", fetchall = True)
        for column in columns:
            info = database.execute(f"SELECT {column[1]} FROM ideas WHERE id = '{idea_id[0]}'")
            if column[2] == "BLOB":
                info = json.loads(info[0])
            else:
                info = info[0]
            idea.update({column[1]: info})
        ideas.update({idea_id[0]:idea})
    return ideas