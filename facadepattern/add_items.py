from facadepattern.bootstrap import Bootstrap

class AddItems(Bootstrap):

    def __init__(self, items):
        self.items = items
        self.state = "Start"

    def bootstrap(self):
        self.state = "Executed"
        print(self.add_items())

    def add_items(self):
        # Sort self.items
        return sum(self.items)
