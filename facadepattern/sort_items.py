from facadepattern.bootstrap import Bootstrap

class SortItems(Bootstrap):

    def __init__(self, items):
        self.items = items
        self.state = "Start"

    def bootstrap(self):
        self.state = "Executed"
        print(self.sort_items())

    def sort_items(self):
        # Sort self.items
        self.items.sort()
        return self.items