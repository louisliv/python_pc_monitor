import wmi
import json
import socket

def get_sensor_values(config):
    wmi_values = wmi.WMI(namespace="root\OpenHardwareMonitor")
    sensors = wmi_values.Sensor()

    return(sensors_to_dict(sensors, config))

def sensors_to_dict(sensors, config):
    ohm_values = {}
    flipped_config = {value: key for key, value in config.items()}

    for sensor in sensors:
        if sensor.Name in flipped_config.keys():
            ohm_values[flipped_config[sensor.Name]] = sensor.Value

    return ohm_values

class ServerSocket:
    def __init__(self, config, sock=None):
        self.config = config
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, 
                socket.SOCK_STREAM
            )
        else:
            self.sock = sock

    def connect_to_server(self):
        try:
            self.sock.connect((self.config['ip'], int(self.config['port'])))
            self.connected = True
            return True
        except TimeoutError as e:
            self.connected = False
            return False

    def send_sensor_data(self):
        totalsent = 0
        try:            
            sensor_values = get_sensor_values(self.config)
            sent = self.sock.sendall(json.dumps(sensor_values).encode('utf-8'))
        except RuntimeError as e:
            print(e)
            self.close_connection()
        except ConnectionResetError as e:
            print(e)
            self.close_connection()

    def close_connection(self):
        self.connected = False
        self.sock.close()
