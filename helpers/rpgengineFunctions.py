import math
import uuid

# какой будет уровень при таком опыте
def get_level(experience: int) -> int:
    level = (-7.5 + math.sqrt(56.25 + 10.5*experience)) / 5.25
    return int(level)

# сколько надо опыта для этого уровня
def get_experience(level: int) -> int:
    experience = 1.5*level * (1.75*level + 5)
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
    return id
