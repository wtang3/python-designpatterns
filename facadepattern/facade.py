from facadepattern.add_items import AddItems
from facadepattern.sort_items import SortItems

class Facade:
    def __init__(self, l):
        self.add_items = AddItems(l)
        self.sort_items = SortItems(l)

    def start(self):
        [a.bootstrap() for a in (self.add_items, self.sort_items)]

    def state(self):
        states = []
        for value in (self.add_items.state, self.sort_items.state):
            states.append(value)

        return states