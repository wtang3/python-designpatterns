from facadepattern.facade import Facade
import unittest
import sys

class Tests(unittest.TestCase):

    def test_facade_pattern(self):
        facade = Facade([4,2,3])
        facade.start()
        states = facade.state()
        self.assertListEqual(states, ['Executed', 'Executed'], "Bootstrap did not run all commands")


if __name__ == '__main__':
    unittest.main()
