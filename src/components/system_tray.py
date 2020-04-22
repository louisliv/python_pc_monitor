from wx.adv import TaskBarIcon
import wx
import os

class SystemTray(TaskBarIcon):    
    def __init__(self, frame):
        TaskBarIcon.__init__(self)
        self.frame = frame

        parent_dir = os.getcwd()
        icon_file_path = os.path.join(parent_dir, 'src\\assets\computer.png')
        
        img = wx.Image(icon_file_path, wx.BITMAP_TYPE_ANY)
        bmp = wx.Bitmap(img)
        self.icon = wx.Icon()
        self.icon.CopyFromBitmap(bmp)
        
        self.SetIcon(self.icon, "Restore")
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)

    def OnTaskBarActivate(self, evt):
        pass

    def OnTaskBarClose(self, evt):
        self.frame.Close()

    def OnTaskBarLeftClick(self, evt):
        self.frame.Show()
        self.frame.Restore()