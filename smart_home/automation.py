import json
import os
class SmartHome:
    def __init__(self):
        self.devices = []
        self.sensors = []
        self.rules = []

    def add_device(self, device):
        self.devices.append(device)

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def add_rule(self, rule):
        self.rules.append(rule)

    def auto_run(self, duration):
        for t in range(duration):
            print(f"\n[INFO] Time {t+1}s:")
            for rule in self.rules:
                value = rule.sensor.read()
                print(f"{rule.sensor.room} {rule.sensor.type}: {value:.2f}")
                if rule.action == "ON" and value >= rule.threshold:
                    rule.device.turn_on()
                elif rule.action == "OFF" and value < rule.threshold:
                    rule.device.turn_off()


class AutomationRule:
    def __init__(self, device, sensor, threshold, action):
        self.device = device
        self.sensor = sensor
        self.threshold = threshold
        self.action = action  # "ON" or "OFF"
        
def save_rules(home):
    rules_data = []
    for rule in home.rules:
        rules_data.append({
            "device": rule.device.name,
            "room": rule.device.room,
            "sensor": rule.sensor.type,
            "threshold": rule.threshold,
            "action": rule.action
        })

    os.makedirs("dataset", exist_ok=True)

    with open("dataset/rules.json", "w") as f:
        json.dump(rules_data, f, indent=4)


def load_rules(home):
    if not os.path.exists("dataset/rules.json"):
        return

    with open("dataset/rules.json", "r") as f:
        rules_data = json.load(f)

    for r in rules_data:
        device = next((d for d in home.devices if d.name == r["device"] and d.room == r["room"]), None)
        sensor = next((s for s in home.sensors if s.type == r["sensor"] and s.room == r["room"]), None)

        if device and sensor:
            home.add_rule(AutomationRule(device, sensor, r["threshold"], r["action"]))