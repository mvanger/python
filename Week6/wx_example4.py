import wx

class MyFrame(wx.Frame):
  def __init__(self, parent, title, *args, **kwargs):
    wx.Frame.__init__(self, parent, *args, title=title, size=(200, 100), **kwargs)
    self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
    self.Show(True)

app = wx.App(False)
frame = MyFrame(None, 'small editor')
app.MainLoop()