from observerpattern.game_stat_absobserver import GameStateAbsObserver

class GameStatePlayerObserver(GameStateAbsObserver):

    def __init__(self, subject):
        self.subject = subject
        self.score = 0
        subject.attach(self)

    def update(self):
        self.score = self.subject.get_score()
        self.show_stats()

    def show_stats(self):
        print("Hi Score for Player {}".format(self.score))