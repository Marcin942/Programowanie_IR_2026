import random

class Character:
    def __init__(self, hp, armor):
        self.hp = hp
        self.armor = armor

    def attack(self, player2):
        # Mnożnik z zadania 3
        mnoznik = random.randint(1, 6)
        obrazenia = max(5 * mnoznik - player2.armor, 0)
        player2.hp -= obrazenia
        print(f"Zadano {obrazenia} obrażeń!")

    def heal(self):
        mnoznik = random.randint(1, 6)
        leczenie = 1 * mnoznik
        self.hp += leczenie
        print(f"Uleczono się o {leczenie} HP.")

    def special_attack(self, player2):
        pass

class Warrior(Character):
    def __init__(self):
        super().__init__(hp=10, armor=3)

    def special_attack(self, player2):
        mnoznik = random.randint(1, 6)
        redukcja = 1 * mnoznik
        player2.armor -= redukcja
        print(f"Pancerz przeciwnika zniszczony o {redukcja}!")

class Druid(Character):
    def __init__(self):
        super().__init__(hp=10, armor=1)

    def special_attack(self, player2):
        mnoznik = random.randint(1, 6)
        kradziez = 3 * mnoznik
        player2.hp -= kradziez
        self.hp += kradziez
        print(f"Skradziono {kradziez} HP!")

    def heal(self):
        mnoznik = random.randint(1, 6)
        leczenie = 3 * mnoznik
        self.hp += leczenie
        print(f"Druid uleczył się o {leczenie} HP.")

def gra():
    gracz1 = Warrior()
    gracz2 = Druid()
    
    print("START GRY: Wojownik vs Druid")
    
    while gracz1.hp > 0 and gracz2.hp > 0:
        print("\n--- Tura Wojownika (Gracz 1) ---")
        wybor1 = input("Wybierz akcję (1 - atak, 2 - atak specjalny, 3 - leczenie): ")
        if wybor1 == "1":
            gracz1.attack(gracz2)
        elif wybor1 == "2":
            gracz1.special_attack(gracz2)
        elif wybor1 == "3":
            gracz1.heal()
        else:
            print("Pusty ruch!")

        if gracz2.hp <= 0:
            break
            
        print("\n--- Tura Druida (Gracz 2) ---")
        wybor2 = input("Wybierz akcję (1 - atak, 2 - atak specjalny, 3 - leczenie): ")
        if wybor2 == "1":
            gracz2.attack(gracz1)
        elif wybor2 == "2":
            gracz2.special_attack(gracz1)
        elif wybor2 == "3":
            gracz2.heal()
        else:
            print("Pusty ruch!")

        print(f"\n--- STAN HP: Wojownik = {gracz1.hp}, Druid = {gracz2.hp} ---")
        
    print("\nKONIEC GRY!")
    if gracz1.hp > 0:
        print("Wygrał Wojownik!")
    else:
        print("Wygrał Druid!")

if __name__ == "__main__":
    gra()