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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 338,300 ), wx.DefaultSize )

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


        bSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer3.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )


        bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        self.bar = wx.MenuBar( 0 )
        self.info_bar = wx.Menu()
        self.standart_men = wx.MenuItem( self.info_bar, wx.ID_ANY, _(u"Standart"), wx.EmptyString, wx.ITEM_NORMAL )
        self.info_bar.Append( self.standart_men )

        self.hardware_men = wx.MenuItem( self.info_bar, wx.ID_ANY, _(u"Hardware"), wx.EmptyString, wx.ITEM_NORMAL )
        self.info_bar.Append( self.hardware_men )

        self.windows_men = wx.MenuItem( self.info_bar, wx.ID_ANY, _(u"Windows"), wx.EmptyString, wx.ITEM_NORMAL )
        self.info_bar.Append( self.windows_men )

        self.extra_men = wx.MenuItem( self.info_bar, wx.ID_ANY, _(u"Extra"), wx.EmptyString, wx.ITEM_NORMAL )
        self.info_bar.Append( self.extra_men )

        self.bar.Append( self.info_bar, _(u"Info") )

        self.mngr_bar = wx.Menu()
        self.task_mngr_men = wx.MenuItem( self.mngr_bar, wx.ID_ANY, _(u"Self-Made (Warning ressource heavy)"), wx.EmptyString, wx.ITEM_NORMAL )
        self.mngr_bar.Append( self.task_mngr_men )

        self.task_mngr_win_men = wx.MenuItem( self.mngr_bar, wx.ID_ANY, _(u"Windows"), wx.EmptyString, wx.ITEM_NORMAL )
        self.mngr_bar.Append( self.task_mngr_win_men )

        self.bar.Append( self.mngr_bar, _(u"Task Manger") )

        self.settings_bar = wx.Menu()
        self.m_menuItem7 = wx.MenuItem( self.settings_bar, wx.ID_ANY, _(u"System controll"), wx.EmptyString, wx.ITEM_NORMAL )
        self.settings_bar.Append( self.m_menuItem7 )

        self.bar.Append( self.settings_bar, _(u"Settings") )

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
        self.Bind( wx.EVT_MENU, self.activate_task_mngr_men, id = self.task_mngr_men.GetId() )
        self.Bind( wx.EVT_MENU, self.activate_task_mngr_win_men, id = self.task_mngr_win_men.GetId() )
        self.Bind( wx.EVT_MENU, self.activate_sys_cntr_men, id = self.m_menuItem7.GetId() )

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

    def activate_task_mngr_men( self, event ):
        event.Skip()

    def activate_task_mngr_win_men( self, event ):
        event.Skip()

    def activate_sys_cntr_men( self, event ):
        event.Skip()


