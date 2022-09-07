class Basket:
    def __init__(self):
        self.fruits = set()

    def add_fruit(self, fruit_name):
        self.fruits.add(fruit_name)

    def display_fruits(self):
        for fruit in self.fruits:
            print(fruit)