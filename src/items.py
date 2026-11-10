from dice import Dice

class Weapon:
    """Contains logic for weapon items"""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """Creates a named weapon with a damage value"""

        # set weapon name and damage
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Rolls damage by calling Dice"""
        # gets a damage roll for weapon by calling Dice.roll()
        return self.damage_dice.roll()

# example weapon
# weapon1 = Weapon("Ax", Dice())

# print(weapon1)
# print(weapon1.roll_damage())
