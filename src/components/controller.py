import json
import time

from lib.io import ServerSocket
import wx

class AppController():
    def __init__(
        self, 
        config=None, 
        config_path=None, 
        text_fields=None
    ):
        super().__init__()
        self.config = config
        self.config_path = config_path
        self.text_fields = text_fields

    def handle_set_config(self, event):
        self.set_config()

        f = open(self.config_path, "w")
        f.write(json.dumps(self.config))
        f.close()

    def handle_connect(self, event):
        if event.GetEventObject().GetValue():
            socket = ServerSocket(self.config)
            event.GetEventObject().SetLabel('Connecting...')
            try:
                socket.connect_to_server()
                event.GetEventObject().SetLabel('Connected')
            except:
                msg_box = wx.MessageDialog(
                    None,
                    'Server Connection Refused', 
                    'PC Monitor Connect', 
                    wx.OK | wx.ICON_WARNING
                )
                msg_box.ShowModal()
                event.GetEventObject().SetLabel('Connect')
                event.GetEventObject().SetValue(False)
                return

            while True:
                try:
                    socket.send_sensor_data()
                    time.sleep(int(self.config['refresh']) / 1000)
                except:
                    msg_box = wx.MessageDialog(
                        None,
                        'Server Connection Closed', 
                        'PC Monitor Connect', 
                        wx.OK | wx.ICON_WARNING
                    )
                    msg_box.ShowModal()
                    break
        
        socket.close_connection()
        event.GetEventObject().SetValue(False)
        event.GetEventObject().SetLabel('Connect')

    def set_config(self):
        for key, text_field in self.text_fields.items():
            current = text_field.GetLineText(0)
            self.config[key] = current