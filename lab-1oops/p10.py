class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, qty, price):
        self.items[name] = (qty, price)

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError(name)
        del self.items[name]

    def total_value(self):
        return sum(q * p for q, p in self.items.values())

    def __len__(self):
        return len(self.items)


inv = Inventory()

with open("stock.txt", "r") as f:
    for line in f:
        try:
            name, qty, price = line.strip().split(",")
            inv.add_item(name, int(qty), int(price))
        except ValueError:
            print("Skipping bag: bad number")

print(len(inv), "items, total value", inv.total_value())

inv.remove_item("pen")
print(len(inv), "items, total value", inv.total_value())

try:
    inv.remove_item("laptop")
except KeyError:
    print("Error: 'No item named laptop'")