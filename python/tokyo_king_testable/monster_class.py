# Monster with unittest and populated into King of Tokyo game.
# https://boardgamegeek.com/boardgame/144790/ANGRY-dice
# >>>-------------------------------------------------------->
__author__ = 'mw'


class Monster():
    """ Create a monster based off UML using TDD. """

    def __init__(self, name):
        """ Initializes the Monster class. """
        self.name = name  # set on init
        self.status = "Out of Tokyo"
        self.health = 10
        self.victory_points = 0  # >= 20 points is "WINNING"

    def reset(self):
        """ Reset Monster to initial stats. """
        self.status = "Out of Tokyo"
        self.health = 10
        self.victory_points = 0

    def in_tokyo(self):
        """ Returns True if Monster status "in Tokyo". """
        return True if self.status == "in Tokyo" else False

    def flee(self):
        """
        Prompts Monster to see if they want to flee Tokyo.
        If 'y', return True
        If 'n', return False
        """
        # self.userInput = input("Flee to Tokyo, enter 'y' or 'n': ").lower()
        # if "y" in self.userInput:
        #     return True
        # elif "n" in self.userInput:
        #     return False
        # else:
        #     print("I do not understand")

    def heal(self):
        """
        Add the passed integer to the Monster's health,
        up to but not exceeding 10.
        """
        pass

    def attack(self):
        """
        Subtract the passed integer from the Monster's health,
        returning health. If health is <= 0, set status to "K.O.'d".
        """
        pass

    def score(self):
        """
        Add passed integer to Monster's victory_points, and
        return victory_points. If a Monster's VP >= 20,
        set status to "WINNING".
        """
        pass


if __name__ == '__main__':
    monster = Monster("Cereal Killer")