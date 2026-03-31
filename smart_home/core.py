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