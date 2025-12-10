# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class gui_box
###########################################################################

class gui_box ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.gui_list = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT )
        bSizer2.Add( self.gui_list, 1, wx.ALL|wx.EXPAND, 5 )


        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button1 = wx.Button( self, wx.ID_ANY, _(u"MyButton"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.m_button1, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        self.bar = wx.MenuBar( 0 )
        self.expose = wx.Menu()
        self.standart_men = wx.MenuItem( self.expose, wx.ID_ANY, _(u"Standart"), wx.EmptyString, wx.ITEM_NORMAL )
        self.expose.Append( self.standart_men )

        self.hardware_men = wx.MenuItem( self.expose, wx.ID_ANY, _(u"Hardware"), wx.EmptyString, wx.ITEM_NORMAL )
        self.expose.Append( self.hardware_men )

        self.windows_men = wx.MenuItem( self.expose, wx.ID_ANY, _(u"Windows"), wx.EmptyString, wx.ITEM_NORMAL )
        self.expose.Append( self.windows_men )

        self.extra_men = wx.MenuItem( self.expose, wx.ID_ANY, _(u"Extra"), wx.EmptyString, wx.ITEM_NORMAL )
        self.expose.Append( self.extra_men )

        self.bar.Append( self.expose, _(u"Filter") )

        self.SetMenuBar( self.bar )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_MENU, self.active_standart, id = self.standart_men.GetId() )
        self.Bind( wx.EVT_MENU, self.active_hardware, id = self.hardware_men.GetId() )
        self.Bind( wx.EVT_MENU, self.active_windows, id = self.windows_men.GetId() )
        self.Bind( wx.EVT_MENU, self.active_extra, id = self.extra_men.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def active_standart( self, event ):
        event.Skip()

    def active_hardware( self, event ):
        event.Skip()

    def active_windows( self, event ):
        event.Skip()

    def active_extra( self, event ):
        event.Skip()


