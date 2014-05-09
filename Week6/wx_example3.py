import wx

app = wx.App()
frame1 = wx.Frame(None, -1, 'Hello world parent')

frame2 = wx.Frame(frame1, -1, 'Hello world child')
frame1.Show()
frame2.Show()
app.MainLoop()