#!/usr/bin/env python
#coding=utf-8
import wx.lib.iewin
import wx,time

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent = None,id = -1,pos = wx.DefaultPosition,title = u'iewinsd')
        panel = wx.Panel(self)
        self.html = wx.lib.iewin.IEHtmlWindow(panel,-1,pos = wx.DefaultPosition,style = 0,name = 'OK')
        self.html.LoadUrl('http://www.python.org')
        self.html
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.html,1, wx.ALL|wx.EXPAND,0)
        panel.SetSizer(sizer)
        sizer.Fit(self)
        self.html.AddEventSink(self)
    def DocumentComplete(self,pDisp,URL):
        s = self.html.GetText()
        print S

if __name__=='__main__':
    app= wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()

