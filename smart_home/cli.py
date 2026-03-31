import argparse
from smart_home.core import Sensor, Device
from .automation import SmartHome, AutomationRule, save_rules, load_rules
import random
import time

def main():
    parser = argparse.ArgumentParser(description="Smart Home Simulator CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list-rules")
    auto_parser = subparsers.add_parser("auto-run")
    auto_parser.add_argument("--duration", type=int, default=10)

    status_parser = subparsers.add_parser("auto-status")
    status_parser.add_argument("--duration", type=int, default=5)

    read_parser = subparsers.add_parser("read-sensor")
    read_parser.add_argument("sensor_type", choices=["temperature", "humidity", "light"])
    read_parser.add_argument("--room", required=True)
    read_parser.add_argument("--duration", type=int, default=5)
 #########
    rule_parser = subparsers.add_parser("set-rule", help="Add a new automation rule")
    rule_parser.add_argument("--device", required=True)
    rule_parser.add_argument("--room", required=True)
    rule_parser.add_argument("--sensor", required=True)
    rule_parser.add_argument("--threshold", type=float, required=True)
    rule_parser.add_argument("--action", choices=["ON", "OFF"], required=True)

 

    args = parser.parse_args()

    # Initialize SmartHome
    home = SmartHome()
    temp_sensor = Sensor("temperature", "LivingRoom")
    light_sensor = Sensor("light", "Kitchen")
    fan = Device("Fan", "LivingRoom")
    light = Device("Light", "Kitchen")

    home.add_sensor(temp_sensor)
    home.add_sensor(light_sensor)
    home.add_device(fan)
    home.add_device(light)
   

    # automation rules
    home.add_rule(AutomationRule(fan, temp_sensor, threshold=25, action="ON"))
    home.add_rule(AutomationRule(light, light_sensor, threshold=150, action="ON"))

    
    if args.command == "auto-run":
        home.auto_run(duration=args.duration)

    elif args.command == "read-sensor":
        

        print(f"Reading {args.sensor_type} in {args.room}...\n")

        for i in range(args.duration):
            if args.sensor_type == "temperature":
                value = round(random.uniform(20, 30), 2)
                unit = "°C"
            elif args.sensor_type == "humidity":
                value = random.randint(40, 70)
                unit = "%"
            else:
                value = random.randint(50, 300)
                unit = "lux(brightness)"

            print(f"[{i+1}] {args.sensor_type.capitalize()}: {value} {unit}")
            time.sleep(1)
    elif args.command == "auto-status":

        print("Starting smart home status monitoring...\n")

        for i in range(args.duration):
            temp = round(random.uniform(20, 30), 2)
            light = random.randint(50, 300)

            ac_status = "ON" if temp > 25 else "OFF"
            light_status = "ON" if light < 100 else "OFF"

            print(f"[{i+1}] Temp: {temp}°C → AC: {ac_status} | Light: {light} lux → Lights: {light_status}")

            time.sleep(1)
    elif args.command == "set-rule":
        device_name = args.device
        room_name = args.room
        sensor_type = args.sensor
        threshold = args.threshold
        action = args.action

        # Find the device and sensor objects
        #device = home.get_device(device_name, room_name)
        #sensor = home.get_sensor(sensor_type, room_name)
        device = None
        for d in home.devices:
            if d.name == device_name and d.room == room_name:
                device = d    

        sensor = None
        for s in home.sensors:
            if s.type == sensor_type and s.room == room_name:
                sensor = s       

        if device and sensor:
            home.add_rule(AutomationRule(device, sensor, args.threshold, args.action))
            save_rules(home)   # ✅ ADD THIS
            print(f"Rule added: {device.name} → {args.action} when {sensor.type} > {args.threshold}")
        else:
            print("Error: Device or sensor not found")

    

    elif args.command == "list-rules":
        if not home.rules:
            print("No rules defined.")
        else:
            for i, rule in enumerate(home.rules, 1):
                print(f"{i}. {rule.device.name} → {rule.action} when {rule.sensor.type} > {rule.threshold}")