import random

class Dice:
    """Creates a rollable n-sided die"""

    def __init__(self, sides: int = 6) -> None:
        """
        Creates a rollable n-sided die
        
        Args:
            sides: how many sides the die should have. Default 6.
        """
        if sides >= 2:
            self.sides = sides
        else:
            print("Please input a integer greater than or equal to 2")

    def roll(self) -> int:
        """Rolls a random number for the dice"""
        # returns a random nunmber between 1 and size of die
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Representation of die"""
        return f"Dice(sides=6)"

    def __str__(self) -> str:
        """Representation of die"""
        return f"Dice(sides=6)"

    def __call__(self) -> int:
        """Rolls the specified die when object is called"""
        return self.roll()

# exapmle d20
# d20 = Dice(20)
# print(Dice(10).roll())
# print(d20())