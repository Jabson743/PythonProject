class Television:

    def __init__(self):
        self.channel: int = 100
        self.volume_level: int = 10
        self.isOn = False

    def televisionPowerOn(self):
         self.isOn = True

    def televisionPowerOff(self):
        self.isOn = True

    def televisionIsOn(self):
        return self.isOn

    def televisionCanGetChannel(self):
        if self.channel == 100:
            return self.channel

    def televisionChannelUp(self, channel):
        self.channel = channel
        if self.channel == 100:
            self.channel += 1
            return self.channel








