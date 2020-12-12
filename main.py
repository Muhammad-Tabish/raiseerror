class garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_cars(self, car):
         raise NotImplementedError['we cant add cars']

ford = garage()
ford.add_cars('fiesta')
print(len(ford))