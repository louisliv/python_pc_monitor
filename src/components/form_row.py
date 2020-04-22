import wx
from lib.constants import CONSTANTS

class FormRow(wx.BoxSizer):
    def __init__(self, parent=None, text_field=None, config=None):
        super().__init__(wx.HORIZONTAL)

        self.text_ctrl = wx.TextCtrl(parent, value=config[text_field['id']])
        label = wx.StaticText(parent, label=text_field['label'])
        
        self.Add(label, 0, wx.ALL | wx.LEFT, 5)        
        self.Add(self.text_ctrl, flag=wx.RIGHT | wx.RIGHT, border=0)        
                
        parent.text_fields[text_field['id']] = self.text_ctrl 