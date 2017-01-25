from observerpattern.game_stat_subject import GameStatSubject
from observerpattern.game_stat_player_observer import GameStatePlayerObserver

import unittest

class Tests(unittest.TestCase):

    def test_observer_pattern(self):
        subject = GameStatSubject()
        observer = GameStatePlayerObserver(subject)

        subject.set_score(10)
        score = subject.get_score()
        self.assertEquals(score, 10)

        subject.set_score(20)
        score = subject.get_score()
        self.assertEquals(score, 20)

        subject.set_score(30)
        score = subject.get_score()
        self.assertEquals(score, 30)

        # Detach observer
        subject.detach(observer)

if __name__ == '__main__':
    unittest.main()
