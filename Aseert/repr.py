# We will use the __repr__ here

class Car:
    """docstring for ."""
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    # after adding this will see the car directly
    def __repr__(self):
        return 'Car {self.color}, {self.mileage}'.format(self=self)

mycar = Car('red', 34)
print(mycar)

# output
# Car red, 34
