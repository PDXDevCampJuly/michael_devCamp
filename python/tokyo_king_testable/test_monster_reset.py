__author__ = 'mw'

import unittest
from monster_class import Monster


class TestMonsterReset(unittest.TestCase):

    def setUp(self):
        """ Initializes the monster for the following testing functions. """
        self.monster = Monster("Cereal Killer")

    def tearDown(self):
        """ Delete the instance of monster after running tests. """
        del self.monster

    def test_reset_status_to_out_of_tokyo(self):
        """ Reset status to initial value "Out of Tokyo". """
        self.monster.status = "in Tokyo"
        self.monster.reset()
        self.assertEqual("Out of Tokyo", self.monster.status,
                         "reset status to 'Out of Tokyo'")

    def test_reset_health_to_10(self):
        """ Reset health to initial value 10. """
        self.monster.health = 20
        self.monster.reset()
        self.assertEqual(10, self.monster.health, "reset health to 10")

    def test_reset_victory_points_to_0(self):
        """ Reset victory_points to initial value zero. """
        self.monster.victory_points = 20
        self.monster.reset()
        self.assertEqual(0, self.monster.victory_points,
                         "reset victory_points to 0")


if __name__ == '__main__':
    unittest.main()
