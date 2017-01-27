from facadepattern.bootstrap_facade import BootstrapFacade

class AddItems(BootstrapFacade):

    def __init__(self, items):
        self.items = items

    def bootstrap(self):
        print(self.add_items())

    def add_items(self):
        # Sort self.items
        return sum(self.items)
