import numpy as np

class Character:
    def __init__(self, hp, armor):
        self.hp = hp
        self.armor = armor

    def attack(self, player2):
        damage = np.max(5 - player2.armor, 0)
        player2.hp -= damage
        
    def heal(self):
        self.hp += 1
        
    def special_attack(self, player2):
        pass

class Warrior(Character):
    def __init__(self):
        super().__init__(hp = 10, armor = 3)

    def special_attack(self, player2):
        if player2.armor > 0:
            player2.armor -= 1
            print("Wojownik rozbija pancerz przeciwnika")

class Druid(Character):
    def __init__(self):
        super().__init__(hp = 10, armor = 1)

    def special_attack(self, player2):
        damage = 3
        player2.hp -= damage
        self.hp += damage
        print(f"Druid zabiera {damage} HP przeciwnikowi i leczy się")

    def heal(self):
        self.hp += 2

player1 = Warrior()
player2 = Druid()

while player1.hp > 0 and player2.hp > 0:
    action1 = input("Akcja gracza 1 (a - attack / s - special attack, / h - heal): ")
    if action1 == 'a':
        player1.attack(player2)
    elif action1 == 's':
        player1.special_attack(player2)
    elif action1 == 'h':
        player1.heal()

    action2 = input("Akcja gracza 2 (a - attack / s - special attack, / h - heal): ")
    if action2 == 'a':
        player2.attack(player1)
    elif action2 == 's':
        player2.special_attack(player1)
    elif action2 == 'h':
        player2.heal()

    print(f"Gracz 1: {player1.hp} HP")
    print(f"Gracz 2: {player2.hp} HP")

if player1.hp > 0:
    print("Gracz 1 wygrywa")
else:
    print("Gracz 2 wygrywa")
