from observerpattern.game_stat_abssubject import GameStateAbsSubject

class GameStatSubject(GameStateAbsSubject):

    def __init__(self):
        self.score = 0

    def set_score(self, score):
        self.score = score
        self.notify()

    def get_score(self):
        return self.score
