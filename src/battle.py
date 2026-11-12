import game_simulator_v1 as game
import items
from dice import Dice


class Battle:
    """Battle between two characters"""

    def __init__(self, hero: game.Character, enemy: game.Character) -> None:
        """Creates a battle between two characters"""
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """A single round of battle where characters attack each other"""
        self.hero.attack(self.enemy)
        print(f"{self.hero.name} attacked {self.enemy.name}")

        if self.enemy.is_alive is True:
            self.enemy.attack(self.hero)
            return print(f"{self.enemy.name} attacked {self.hero.name}")
        else:
            return print(f"{self.enemy.name} has been defeated")

    def simulate_battle(self) -> str:
        """Start a running battle until one character is no longer alive"""
        while self.hero.is_alive and self.enemy.is_alive is True:
            self.play_round()

        if self.hero.is_alive is True:
            return f"{self.hero.name} deafeted {self.enemy.name} and won"
        else:
            return f"The despicable {self.enemy.name} has deafeted {self.hero.name}"


# # example character with weapon
# ch1 = game.Character("Aria", weapon=items.Weapon("Dagger", Dice(15)))
# # # # print(ch1.attack)

# # # character wihtout a weapon
# ch2 = game.Character("Wolf")

# # ch2.attack(ch1)
# # print(ch1)
# # print(ch2)

# print(Battle(ch1, ch2).simulate_battle())
# # print(Battle(ch1, ch2).play_round())