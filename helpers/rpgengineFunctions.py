import math
import uuid
from time import time
from .randomFunctions import getStrings
from .databaseFunctions import check_user, edit_nplayer, get_item, add_nitem, edit_nitem, delete_nitem, get_item_species, get_species, get_player_inv, get_location

# какой будет уровень при таком опыте
def get_level(experience: int) -> int:
    level = (math.sqrt(10.5*experience + 2304) - 48) / 5.25
    # (-7.5 + math.sqrt(56.25 + 10.5*experience)) / 5.25
    return int(level)

# сколько надо опыта для этого уровня
def get_experience(level: int) -> int:
    experience = 2.625*level*level + 48*level
    # 1.5*level * (1.75*level + 5)
    return math.ceil(experience)

# сколько будет лимит здоровья при таком уровне
def get_max_health(level: int) -> int:
    max_health = 20 + 4.2*level
    return int(max_health)

# вероятность событий при $chance %
def chance(chance: int):
    random_chance = random.random() * 100
    if random_chance > chance:
        result = False
    else:
        result = True
    return result

# генерация id для предметов/мобов
def generate_id():
    id = uuid.uuid4()
    return str(id)

# положительное: лечение
# отрицательное: повреждения
def change_player_health(user_id: str, health: int):
    player = check_user(user_id)
    if not player:
        return "player with <string:id> not exist"
    else:
        next_var = player.get("health") + health
        max_health = get_max_health(get_level(player.get("experience")))
        
        if next_var > max_health:
            health = max_health - player.get("health")
            player["health"] = max_health
        elif next_var < 0:
            health = player.get("health")
            player["health"] = 0
        else:
            player["health"] = next_var
        
        edit_nplayer(player)
        return health

def check_death(user_id: str):
    player = check_user(user_id)
    if not player:
        return "player with <string:id> not exist"
    else:
        if player.get("health") > 0:
            return False
        else:
            return True

# использование предмета
def use_item(item_id: str, count: int = 1):
    item = get_item(item_id)
    
    owner_id = item.get("owner_id")
    owner = check_user(owner_id)
    
    species = get_item_species(item_id)
    iType = species.get("type")
    
    if iType == "food":
        health = change_player_health(owner_id, species["health"]*count)
        item["count"] -= count
        if item.get("count") > 0:
            edit_nitem(item)
        else:
            delete_nitem(item_id)
        return getStrings(str_id = "helpers.rpgengineFunctions.use_item.healed").format(health = health)
    else:
        return "NaN"

# выдать предмет
def add_item(user_id: str, species: str, count: int = 1):
    
    speciesdict = get_species(species)
    if speciesdict.get("is_counts") == True:
        items = [it for it in get_player_inv(user_id).values() if it.get("species") == species]
        if items:
            item = items[0]
            item["count"] += count
            edit_nitem(item)
        else:
            someid = generate_id()
            item = {
                "item_id": someid,
                "species": species,
                "owner_id": user_id,
                "count": count,
                "equipped": False,
                "durability": 0
            }
            add_nitem(item)
    else:
        for i in range(count):
            someid = generate_id()
            item = {
                "item_id": someid,
                "species": species,
                "owner_id": user_id,
                "count": 1,
                "equipped": False,
                "durability": 0
            }
            add_nitem(item)

# True если перешел, иначе False
def move_player(user_id: str, loc_id: str = "void", instant = False):
    
    player = check_user(user_id)
    if not player:
        return "player with <string:id> not exist"
    
    if instant:
        player["location"] = loc_id
        edit_nplayer(player)
        return True
    
    location = get_location(player.get("location"))
    if loc_id in location.get("paths"):
        player["location"] = loc_id
        edit_nplayer(player)
        return True
    else:
        return False

def event_mob_a(user_id: str, instant = False):
    player = check_user(user_id)
    if not player:
        return "player with <string:id> not exist"
    
    location = get_location(player.get("location"))
    if location.get("mobs"):
        if instant:
            ...
            return True
        
        if (player.get("mob_kd") - int(time())) < 0:
            ...
            return True
        
        return False
        
    else:
        return False