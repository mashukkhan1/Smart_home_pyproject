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