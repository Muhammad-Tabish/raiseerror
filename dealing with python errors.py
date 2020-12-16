class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<car {self.make} {self.model}>'


class garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise ValueError(f'tried to add a {car.__class__.__name__} to the garage ')
        self.cars.append(car)

ford = garage ()
fiesta = Car('ford', 'fiesta')

try:
    ford.add_car('fiesta')
except TypeError:
     print('your car was not a car')