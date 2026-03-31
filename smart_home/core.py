import random

class Device:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.state = "OFF"
        self.history = []

    def turn_on(self):
        self.state = "ON"
        self.history.append(1)
        print(f"[INFO] {self.room} {self.name} turned ON")

    def turn_off(self):
        self.state = "OFF"
        self.history.append(0)
        print(f"[INFO] {self.room} {self.name} turned OFF")

class Sensor:
    def __init__(self, type_, room):
        self.type = type_
        self.room = room
        self.history = []

    def read(self):
        # Simple simulated sensor values
        if self.type == "temperature":
            value = random.uniform(20, 30)  # 20°C to 30°C
        elif self.type == "light":
            value = random.randint(50, 300)  # lux
        elif self.type == "humidity":
            value = random.uniform(30, 70)  # %
        else:
            value = 0
        self.history.append(value)
        return value