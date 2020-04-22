import wx
import json
import os

from components.main import MainFrame

this_folder = os.path.dirname(os.path.abspath(__file__))
config_json_path = os.path.join(this_folder, 'lib/config.json')
config_file = open(config_json_path)
config = json.load(config_file)
config_file.close() 

app = wx.App()
frame = MainFrame(
    title="PC Monitor Connect", 
    config=config,
    config_path=config_json_path
)
frame.Show()
app.MainLoop()