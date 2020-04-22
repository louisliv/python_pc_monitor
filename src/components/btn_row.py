import wx
from lib.constants import CONSTANTS

class BtnRow(wx.BoxSizer):
    def __init__(self, parent=None, controller=None):
        super().__init__(wx.HORIZONTAL)

        self.controller = controller

        for button in CONSTANTS['buttons']:
            method_to_call = getattr(
                self.controller, 
                button['method']
            )

            if button['toggle']:
                btn = wx.ToggleButton(
                    parent,
                    label=button['title']
                )
                btn.Bind(wx.EVT_TOGGLEBUTTON, method_to_call)
            else:
                btn = wx.Button(
                    parent,
                    label=button['title']
                )
                btn.Bind(wx.EVT_BUTTON, method_to_call)

            self.Add(btn, 0, wx.ALL | wx.CENTER, 5)            
