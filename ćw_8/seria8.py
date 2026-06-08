class Character:
    def __init__(self, hp, armor):
        self.hp = hp
        self.armor = armor

    def attack(self, other):
        if not isinstance(other, Character):
            return NotImplemented
        damage = max(5 - other.armor, 0)
        other.hp -= damage
        return damage
    def heal(self):
        self.fp += 1
    def special_attack(self, other):
    