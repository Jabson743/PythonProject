from idlelib.editor import get_accelerator

class Bike:
    def __init__(self):
        self.isOn = False
        self.gear = 0
        self.gear_speed = 0

    def turn_on(self):
        self.isOn = True

    def turn_off(self):
        return self.isOn == False

    def get_gear(self):
        return self.gear

    def get_gear_speed(self):
        return self.gear_speed

    def accelerate(self, acceleration):
        if acceleration >= 11 or acceleration <= 20:
             self.gear += acceleration
             self.gear = 1



        if acceleration <= 21 or acceleration <= 30:
            self.gear += acceleration
            self.gear = 2

        if acceleration <= 31 or acceleration <= 40:
            self.gear += acceleration
            self.gear = 3

        if acceleration <= 41 or acceleration <= 50:
            self.gear += acceleration
            self.gear = 4

    def decelerate(self, deceleration):
        if deceleration >= 11 or deceleration <= 20:
             self.gear -= deceleration
             self.gear = 1

        if deceleration <= 21 or deceleration <= 30:
            self.gear -= deceleration
            self.gear = 2

        if deceleration <= 31 or deceleration <= 40:
            self.gear -= deceleration
            self.gear = 3

        if deceleration <= 41 or deceleration <= 50:
            self.gear -= deceleration
            self.gear = 4









