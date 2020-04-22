import wmi
import json
import os

def get_sensor_values():
    wmi_values = wmi.WMI(namespace="root\OpenHardwareMonitor")
    sensors = wmi_values.Sensor()

    return(sensors_to_dict(sensors))

def sensors_to_dict(sensors):
    this_folder = os.path.dirname(os.path.abspath(__file__))
    config_json_path = os.path.join(this_folder, 'config.json')
    config_file = open(self.config_json_path)
    config = json.load(config_file)
    config_file.close()

    ohm_values = {}
    config_values = config.values()
    for sensor in sensors:
        if sensor.Name in config_values:
            ohm_values[sensor.Name] = sensor.Value

    return ohm_values