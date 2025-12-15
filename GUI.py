# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class gui_box
###########################################################################

class gui_box ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 499,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.gui_box = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,500 ), 0 )

        # Grid
        self.gui_box.CreateGrid( 2, 2 )
        self.gui_box.EnableEditing( False )
        self.gui_box.EnableGridLines( True )
        self.gui_box.EnableDragGridSize( False )
        self.gui_box.SetMargins( 0, 0 )

        # Columns
        self.gui_box.SetColSize( 0, 196 )
        self.gui_box.SetColSize( 1, 196 )
        self.gui_box.EnableDragColMove( False )
        self.gui_box.EnableDragColSize( False )
        self.gui_box.SetColLabelSize( wx.grid.GRID_AUTOSIZE )
        self.gui_box.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.gui_box.SetRowSize( 0, 25 )
        self.gui_box.SetRowSize( 1, 25 )
        self.gui_box.AutoSizeRows()
        self.gui_box.EnableDragRowSize( True )
        self.gui_box.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.gui_box.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer2.Add( self.gui_box, 1, wx.ALL|wx.EXPAND, 5 )


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
        self.Bind( wx.EVT_ACTIVATE, self.activate_window_activate )
        self.Bind( wx.EVT_ICONIZE, self.activate_window_icon )
        self.Bind( wx.EVT_MAXIMIZE, self.activate_window_max )
        self.Bind( wx.EVT_MOTION, self.activate_window_move )
        self.Bind( wx.EVT_MOVE_END, self.activate_window_end )
        self.Bind( wx.EVT_MOVE_START, self.activate_window_start )
        self.Bind( wx.EVT_SIZE, self.activate_window_size )
        self.Bind( wx.EVT_MENU, self.active_standart, id = self.standart_men.GetId() )
        self.Bind( wx.EVT_MENU, self.active_hardware, id = self.hardware_men.GetId() )
        self.Bind( wx.EVT_MENU, self.active_windows, id = self.windows_men.GetId() )
        self.Bind( wx.EVT_MENU, self.active_extra, id = self.extra_men.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def activate_window_activate( self, event ):
        event.Skip()

    def activate_window_icon( self, event ):
        event.Skip()

    def activate_window_max( self, event ):
        event.Skip()

    def activate_window_move( self, event ):
        event.Skip()

    def activate_window_end( self, event ):
        event.Skip()

    def activate_window_start( self, event ):
        event.Skip()

    def activate_window_size( self, event ):
        event.Skip()

    def active_standart( self, event ):
        event.Skip()

    def active_hardware( self, event ):
        event.Skip()

    def active_windows( self, event ):
        event.Skip()

    def active_extra( self, event ):
        event.Skip()


