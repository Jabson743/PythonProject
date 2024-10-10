import unittest
from Python_Practices import bike
from Python_Practices.bike import Bike

class TestBike(unittest.TestCase):
    def setUp(self):
        self.bike = Bike()

    def test_that_bike_exist(self):
        bike = Bike()
        bike.turn_on()
        self.assertTrue(bike.isOn)

    def test_that_bike_turn_on(self):
        bike = Bike()
        bike.turn_on()
        self.assertTrue(bike.isOn)

    def test_that_bike_turn_off(self):
        bike = Bike()
        bike.turn_on()
        self.assertTrue(bike.isOn)
        bike.turn_off()
        self.assertTrue(bike.isOn)

    def test_that_bike_can_be_accelerated_when_on_gear_one(self):
        bike = Bike()
        bike.turn_on()
        self.assertTrue(bike.isOn)
        bike.accelerate(15)
        self.assertTrue(bike.isOn, bike.accelerate(16))

    def test_that_bike_can_be_accelerated_when_on_gear_two(self):
        bike = Bike()
        bike.turn_on()
        self.assertTrue(bike.isOn)
        bike.accelerate(24)
        self.assertTrue(bike.isOn, bike.accelerate(26))

    def test_that_bike_can_be_accelerated_when_on_gear_three(self):
        bike = Bike()
        bike.turn_on()
        self.assertTrue(bike.isOn)
        bike.accelerate(36)
        self.assertTrue(bike.isOn, bike.accelerate(38))

    def test_that_bike_can_be_accelerated_when_on_gear_four(self):
        bike = Bike()
        bike.turn_on()
        self.assertTrue(bike.isOn)
        bike.accelerate(36)
        self.assertTrue(bike.isOn, bike.accelerate(38))

    def test_that_bike_can_be_decelerated_when_on_gear_one(self):
        bike = Bike()
        bike.turn_on()
        self.assertTrue(bike.isOn)
        bike.decelerate(15)
        self.assertTrue(bike.isOn, bike.decelerate(14))

    def test_that_bike_can_be_decelerated_when_on_gear_two(self):
        bike = Bike()
        bike.turn_on()
        self.assertTrue(bike.isOn)
        bike.decelerate(24)
        self.assertTrue(bike.isOn, bike.decelerate(22))

    def test_that_bike_can_be_decelerated_when_on_gear_three(self):
        bike = Bike()
        bike.turn_on()
        self.assertTrue(bike.isOn)
        bike.decelerate(35)
        self.assertTrue(bike.isOn, bike.decelerate(32))

    def test_that_bike_can_be_decelerated_when_on_gear_four(self):
        bike = Bike()
        bike.turn_on()
        self.assertTrue(bike.isOn)
        bike.decelerate(44)
        self.assertTrue(bike.isOn, bike.decelerate(40))

    def test_that_bike_can_change_gear_speed_in_gear_one(self):
        bike = Bike()
        bike.turn_on()
        self.assertTrue(bike.isOn)
        bike.gear_speed(20)










