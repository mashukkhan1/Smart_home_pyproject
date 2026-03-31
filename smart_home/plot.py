import matplotlib.pyplot as plt

def plot_sensor(sensor):
    plt.plot(sensor.history, label=f"{sensor.room} {sensor.type}")
    plt.xlabel("Time (hr)")
    plt.ylabel(f"{sensor.type}")
    plt.title(f"{sensor.type.capitalize()} readings over time")
    plt.legend()
    plt.show()

def plot_devices(devices):
    for device in devices:
        plt.step(range(len(device.history)), device.history, where="post", label=f"{device.room} {device.name}")
    plt.xlabel("Time (hr)")
    plt.ylabel("State (ON=1/OFF=0)")
    plt.title("Device ON/OFF history")
    plt.legend()
    plt.show()