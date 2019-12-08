import datetime
from freezegun import freeze_time
from math import pi
from time import sleep

class Bubble: # creating the Bubble class with a possibility to add and subtract 2 bubbles, check their radius and capacity

    inst_id = 0 # setting the instance id value to zero
    creation_log = {} # empty log dictionary

    # creating logger method for the class in order to make records to creation_log
    # when new instance of Bubble class is created
    @classmethod
    def creation_logger(cls, creation_time):
        cls.creation_log[cls.inst_id] = creation_time
        cls.inst_id += 1
        return cls.creation_log

    def __init__(self, radius=None, capacity=None):
        if radius is None:
            self.capacity = capacity
            self.radius = ((3*self.capacity)/(4*pi))**(1/3)
            self.id = Bubble.inst_id
            Bubble.creation_logger(self._get_date())
        else:
            self.radius = radius
            self.capacity = (4*pi*(self.radius**3))/3
            self.id = Bubble.inst_id
            Bubble.creation_logger(self._get_date())

    @staticmethod 
    def _get_date(): # static method for getting current time
        return datetime.datetime.now()

    @property
    def square(self):
        square = 4*pi*(self.radius**2)
        return square

    #setting the rules for addition and subtraction of
    #two spheres and returning new sphere object as a result

    def __add__(self, other):
        return Bubble(self.radius + other.radius)

    def __sub__(self, other):
        if self.radius >= other.radius:
            return Bubble(self.radius - other.radius)
        else:
            raise ValueError("Cannot set negative value for a radius")

# Printing creation log for 4 instances of the class
a = Bubble(None, 1)
sleep(0.5)
b = Bubble(None, 4)
sleep(0.5)
c = a + b
sleep(0.5)
d = b - a
print(Bubble.creation_log)

# Tests for time value in the creation log
with freeze_time('2019-01-20 06:06:06'):
    a = Bubble(None, 1)
    assert Bubble.creation_log[0] == datetime.datetime.now()
    b = Bubble(None, 4)
    assert Bubble.creation_log[1] == datetime.datetime.now()
    c = a + b
    assert Bubble.creation_log[2] == datetime.datetime.now()
    assert (c.id - b.id) == 1 # this is for checking if creation_logger() method was called only once
    d = b - a
    assert Bubble.creation_log[3] == datetime.datetime.now()
