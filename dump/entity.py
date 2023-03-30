class Entity():
    def __init__(self):
        self.id = None
        self.name = None
        self.health = None
        self.base_damage = None
        self.base_defence = None
        self.money = None
        self.experience = None
        self.class = None
    
    def attack(self, enemy):
        if self.base_damage >= enemy.base_defence:
            damage = self.base_damage - enemy.base_defence
        else:
            damage = 0
        
        enemy.health -= damage
        
        if enemy.health <= 0:
            return [damage, True]
        else:
            return [damage, False]
    