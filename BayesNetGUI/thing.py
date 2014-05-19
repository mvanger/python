# draw lines, a rounded-rectangle and a circle on a wx.PaintDC() surface
# tested with Python24 and wxPython26     vegaseat      06mar2007
import wx

nodes = ["A", "C", "B"]
parents = [None, None, ["A", "C"]]

class MyFrame(wx.Frame):
    """a frame with a panel"""
    def __init__(self, parent=None, id=-1, title=None):
        wx.Frame.__init__(self, parent, id, title)
        self.panel = wx.Panel(self, size=(800, 750))
        self.panel.Bind(wx.EVT_PAINT, self.on_paint)
        self.Fit()
    def on_paint(self, event):
        # establish the painting surface
        dc = wx.PaintDC(self.panel)
        # dc.SetPen(wx.Pen('blue', 4))
        # # draw a blue line (thickness = 4)
        # dc.DrawLine(50, 20, 300, 20)
        dc.SetPen(wx.Pen('black', 1))
        # draw a red rounded-rectangle
        # rect = wx.Rect(50, 50, 100, 100)
        # dc.DrawRoundedRectangleRect(rect, 50)
        # dc.DrawImageLabel("A", wx.NullBitmap, rect, alignment=100|100)
        # draw a red circle with yellow fill
        dc.SetBrush(wx.Brush('white'))
        # x = 250
        # y = 100
        # r = 50
        # dc.DrawCircle(x, y, r)
        # rect2 = wx.Rect(200, 50, 100, 100)
        # dc.DrawRoundedRectangleRect(rect2, 50)
        # dc.DrawText("C", 245, 95)
        # dc.DrawImageLabel("C", wx.NullBitmap, rect2, alignment=200)

        # rect3 = wx.Rect(125, 175, 100, 100)
        # dc.DrawRoundedRectangleRect(rect3, 50)
        # dc.DrawImageLabel("B", wx.NullBitmap, rect3, alignment=200)

        # dc.DrawLine(150, 100, 200, 100)
        # dc.DrawLine(190, 90, 200, 100)
        # dc.DrawLine(190, 110, 200, 100)

        # w = 50
        # x = 50
        # y = 100
        # z = 100
        # index = 0

        # for n in nodes:
        #     if parents[index] == None:
        #         rect = wx.Rect(w, x, y, z)
        #         dc.DrawRoundedRectangleRect(rect, 50)
        #         dc.DrawImageLabel(n, wx.NullBitmap, rect, alignment=100|100)
        #         # w += 150
        #     else:
        #         w = 50
        #         test = w
        #         rect = wx.Rect(w, x + 150, y, z)
        #         dc.DrawRoundedRectangleRect(rect, 50)
        #         dc.DrawImageLabel(n, wx.NullBitmap, rect, alignment=100|100)
        #         for p in parents[index]:
        #             dc.DrawLine(w + 50, x + 100, test + 50, x + 150)
        #             w += 150
        #     w += 150
        #     index += 1


        # nodes = [u'z', u'x', u'a', u'c', u'b', u'e', u'f']
        # parents = [[], [u'z'], [u'z'], [], [u'a', u'c'], [u'b'], [u'e']]
        nodes = ['a', 'c', 'b']
        parents = [[], [], ['a', 'c']]

        x = 50
        y = 50
        level = 0
        w = 100
        z = 100
        rects = {}
        index = 0

        def drawNode(nodeName):
            rect = wx.Rect(x, y + (150 * level), w, z)
            dc.DrawRoundedRectangleRect(rect, 50)
            dc.DrawImageLabel(nodeName, wx.NullBitmap, rect, alignment=100)

        def drawParentArrow(parentNode):
            # DrawLine arguments are two points: x1, y1, x2, y2
            # Parent node: [x, level]
            dc.DrawLine(parentNode[0] + 50, y + 100 + (150 * parentNode[1]), x + 50, y + (150 * level))
            dc.DrawLine(x + 50, y + (150 * level), x + 40, y - 10 + (150 * level))
            dc.DrawLine(x + 50, y + (150 * level), x + 60, y - 10 + (150 * level))

        for n in nodes:
            for p in parents[index]:
                # check if we need a new level
                if level != rects[p][1] + 1:
                    x = 50
                    level = rects[p][1] + 1
                drawParentArrow(rects[p])
            rects[n] = [x, level]
            drawNode(n)
            x += 150
            index += 1




# test it ...

app = wx.PySimpleApp()
frame1 = MyFrame(title='A Bayesian Network')
frame1.Center()
frame1.Show()
app.MainLoop()