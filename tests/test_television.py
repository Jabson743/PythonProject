import unittest
from Python_Practices import television
from Python_Practices.television import Television


class TestTelevision(unittest.TestCase):
    def setUp(self):
        self.television = Television()

    def test_that_television_exist(self):
        television = Television()
        self.assertFalse(self.television.televisionPowerOn())

    def test_that_television_can_be_turned_on(self):
        television = Television()
        self.assertFalse(television.televisionIsOn())
        television.televisionPowerOn()
        self.assertTrue(television.televisionIsOn())

    def test_that_television_can_be_turned_off(self):
        television = Television()
        self.assertFalse(television.televisionIsOn())
        television.televisionPowerOff()
        self.assertTrue(television.televisionIsOn())

    def test_that_television_can_get_channel(self):
        television = Television()
        self.assertFalse(television.televisionIsOn())
        television.televisionCanGetChannel()
        self.assertTrue(television.televisionCanGetChannel())

    def test_that_television_can_set_channel(self):
        television = Television()
        self.assertFalse(television.televisionIsOn())
        television.televisionCanGetChannel()
        self.assertTrue(television.televisionCanGetChannel())
        television.televisionChannelUp(45)
        self.assertTrue(television.televisionChannelUp(46))













