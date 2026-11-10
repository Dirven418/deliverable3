# Object-oriented game simulator
import items
from dice import Dice

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: items.Weapon = None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def take_damage(self, amount: int) -> None:
        """Take damage and reduce players HP"""
        self._hp -= amount
        self._hp = max(self._hp, 0)

    def heal(self, amount: int) -> None:
        """Heal and increase players HP"""
        self._hp += amount
        self._hp = min(self._hp, self.hp_max)

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        if self.weapon is None:
            target.take_damage(self.damage)
        else:
            target.take_damage(self.weapon.roll_damage())

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Read-only property to check if the character is alive (HP > 0)"""
        return self._hp > 0


# example character with weapon
# ch1 = Character("Aria", weapon=items.Weapon("Dagger", Dice(4)))
# print(ch1.attack)