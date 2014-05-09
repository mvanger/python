import wx

app = wx.App()
for i in range(2):
  frame = wx.Frame(None, title="Hello world %d"%(i+1))
  frame.Show()
app.MainLoop()