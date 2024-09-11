import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.min_attack = 10  # Минимальная сила удара
        self.max_attack = 30  # Максимальная сила удара

    def attack(self, other):
        # Случайная сила удара в диапазоне от min_attack до max_attack
        attack_power = random.randint(self.min_attack, self.max_attack)
        other.health -= attack_power
        print(f"{self.name} атакует {other.name}, нанося {attack_power} урона.")

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self, player_name, computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print("Начинается битва героев!")
        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if not self.computer.is_alive():
                print(f"{self.computer.name} побежден! {self.player.name} победил!")
                break
            self.computer_turn()
            if not self.player.is_alive():
                print(f"{self.player.name} побежден! {self.computer.name} победил!")

    def player_turn(self):
        self.player.attack(self.computer)
        print(f"У {self.computer.name} осталось {self.computer.health} здоровья.\n")

    def computer_turn(self):
        self.computer.attack(self.player)
        print(f"У {self.player.name} осталось {self.player.health} здоровья.\n")


# Пример использования
if __name__ == "__main__":
    game = Game("Игрок")
    game.start()
