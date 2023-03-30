"""
Сила # ненависть hatred
Урон+
Клинки, Рукопашка
# резня, гнев
# massacre, wrath

Интеллект # безумие madness
Мана+
Алхимия, Колдовство
# искажение, безмолвие
# corruption, silence

Ловкость # усталость fatigue
Скорость+
Стрельба, ЛегкиеДоспехи
# террор, суровость
# terror, severity

Выносливость # агония agony
Здоровье+
ТяжелыеДоспехи, Оружейник
# истощение, халтура
# exhaustion, botchery
"""

from entity import Entity

class Player(Entity):
    def __init__(self):
        self.bonus_time = None
        self.location_id = None
        self.in_fight = None
        self.hatred = None
        self.madness = None
        self.fatigue = None
        self.agony = None
        self.massacre = None
        self.wrath = None
        self.corruption = None
        self.silence = None
        self.terror = None
        self.severity = None
        self.exhaustion = None
        self.botchery = None
    