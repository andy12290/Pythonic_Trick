class Car:
    """docstring for ."""
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    # after adding this will see the car directly
    def __str__(self):
        return 'a {self.color} car'.format(self = self)

mycar = Car('red', 34)
print(mycar.color, mycar.mileage)


# lets see the __str__ method
print("Now added__str__: ",mycar)

# __str__: its easy for human user
# __repr__ : not human readable: internal user
