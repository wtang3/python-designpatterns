from facadepattern import bootstrap_facade

class SortItems(bootstrap_facade):

    def __init__(self, items):
        self.items = items

    def bootstrap(self):
        print(self.sort_items())

    def sort_items(self):
        # Sort self.items
        return self.items.sort()