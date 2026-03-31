import argparse
from smart_home.core import Sensor, Device
import random
import time

def main():
    parser = argparse.ArgumentParser(description="Smart Home Simulator CLI")
    subparsers = parser.add_subparsers(dest="command")

  

    read_parser = subparsers.add_parser("read-sensor")
    read_parser.add_argument("sensor_type", choices=["temperature", "humidity", "light"])
    read_parser.add_argument("--room", required=True)
    read_parser.add_argument("--duration", type=int, default=5)
 #########
    

 

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
   



    

    if args.command == "read-sensor":
        

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
    