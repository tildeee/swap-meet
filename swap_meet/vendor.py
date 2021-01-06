class Vendor:

    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        picked_items = []
        for item in self.inventory:
            if item.category is category:
                picked_items.append(item)
        return picked_items

    def swap_first_item(self, other):
        if len(self.inventory) and len(other.inventory):
            my_first_item = self.remove(self.inventory[0])
            their_first_item = other.remove(other.inventory[0])
            self.add(their_first_item)
            other.add(my_first_item)
            return True
        else:
            return False

    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if len(items) == 0:
            return None
        best = items[0]
        for item in items:
            if item.condition > best.condition:
                best = item
        return best

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)

        if my_best and their_best:
            self.inventory.remove(my_best)
            self.inventory.append(their_best)

            other.inventory.remove(their_best)
            other.inventory.append(my_best)
            return True
        else:
            return False

