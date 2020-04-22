import wx

from components.form_row import FormRow
from components.btn_row import BtnRow
from components.system_tray import SystemTray

from lib.constants import CONSTANTS
from components.controller import AppController

class MainFrame(wx.Frame):    
    def __init__(self, title='WX', config=None, config_path=None):
        super().__init__(parent=None, title=title)

        self.config = config
        self.config_path = config_path
        self.text_fields = {}
        self.controller = AppController(
            config=self.config,
            config_path=self.config_path,
            text_fields=self.text_fields
        )
        self.init_ui()


    def init_ui(self):
        panel = wx.Panel(self)
        panel.text_fields = self.text_fields
        
        self.tbIcon = SystemTray(self)
        
        self.Bind(wx.EVT_ICONIZE, self.onMinimize)
        self.Bind(wx.EVT_CLOSE, self.onClose)

        sizer = wx.BoxSizer(wx.VERTICAL)
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add((-1, 10))

        for field_section in CONSTANTS['text_fields_sections']:
            section_label_hbox = wx.BoxSizer(wx.HORIZONTAL)
            section_label = wx.StaticText(
                panel, 
                label=field_section['title']
            )

            font = wx.Font(wx.FontInfo(12))
            section_label.SetFont(font) 

            section_label_hbox.Add(section_label)
            vbox.Add(section_label_hbox, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)
            vbox.Add((-1, 10)) 

            for text_field in field_section['text_fields']:
                form_row = FormRow(
                    parent=panel,
                    text_field=text_field,
                    config=self.config
                )

                vbox.Add(form_row, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)
                vbox.Add((-1, 10))

        vbox.Add((-1, 10))

        self.btn_row = BtnRow(parent=panel, controller=self.controller)
        vbox.Add(self.btn_row, flag=wx.ALIGN_CENTER, border=10)

        # sizer.Add(vbox, flag=wx.EXPAND, border=0)

        panel.SetSizer(vbox)

        btn_row_width, btn_row_height = self.btn_row.GetMinSize()

        width, height = panel.GetBestSize()
        self.SetSize(width=width + 100, height=height + btn_row_height + 10)

        self.Show()

    def onClose(self, evt):
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        self.Destroy()
        
    def onMinimize(self, event):
        print('here')
        if self.IsIconized():
            self.Hide()