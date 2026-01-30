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
import wx.richtext

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

        self.main_button_open_panel_settings = wx.Button( self, wx.ID_ANY, _(u"System Settings"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.main_button_open_panel_settings.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_CAPTIONTEXT ) )
        self.main_button_open_panel_settings.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        bSizer3.Add( self.main_button_open_panel_settings, 0, wx.ALL, 5 )


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
        self.main_button_open_panel_settings.Bind( wx.EVT_BUTTON, self.main_button_open_panel_settings_evnt )
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

    def main_button_open_panel_settings_evnt( self, event ):
        event.Skip()

    def active_standart( self, event ):
        event.Skip()

    def active_hardware( self, event ):
        event.Skip()

    def active_windows( self, event ):
        event.Skip()

    def active_extra( self, event ):
        event.Skip()


###########################################################################
## Class Settings_Dlg
###########################################################################

class Settings_Dlg ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 740,300 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer16 = wx.BoxSizer( wx.VERTICAL )

        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer17.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, _(u"Windows Tools"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        bSizer17.Add( self.m_staticText2, 0, wx.ALL, 5 )


        bSizer17.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer16.Add( bSizer17, 0, wx.EXPAND, 5 )

        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        gSizer1 = wx.GridSizer( 0, 1, 0, 0 )

        self.windows_setting_task_manager_button = wx.Button( self, wx.ID_ANY, _(u"Task Manager"), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.windows_setting_task_manager_button, 0, wx.ALL, 5 )

        self.windows_setting_sys_cntrl_button = wx.Button( self, wx.ID_ANY, _(u"System Control"), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.windows_setting_sys_cntrl_button, 0, wx.ALL, 5 )

        self.windows_setting_perf_rel_button = wx.Button( self, wx.ID_ANY, _(u"Reliability monitoring"), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.windows_setting_perf_rel_button, 0, wx.ALL, 5 )


        bSizer5.Add( gSizer1, 0, wx.EXPAND, 0 )


        bSizer5.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer16.Add( bSizer5, 1, wx.EXPAND, 5 )


        bSizer4.Add( bSizer16, 0, wx.EXPAND, 5 )

        bSizer161 = wx.BoxSizer( wx.VERTICAL )

        bSizer171 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer171.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, _(u"System"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )

        bSizer171.Add( self.m_staticText21, 0, wx.ALL, 5 )


        bSizer171.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer161.Add( bSizer171, 0, wx.EXPAND, 5 )

        bSizer51 = wx.BoxSizer( wx.HORIZONTAL )


        bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        gSizer11 = wx.GridSizer( 0, 1, 0, 0 )

        self.system_setting_bios_button = wx.Button( self, wx.ID_ANY, _(u"Bios"), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.system_setting_bios_button.SetAuthNeeded()
        gSizer11.Add( self.system_setting_bios_button, 0, wx.ALL, 5 )


        bSizer51.Add( gSizer11, 0, wx.EXPAND, 0 )


        bSizer51.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        bSizer161.Add( bSizer51, 1, wx.EXPAND, 5 )


        bSizer4.Add( bSizer161, 1, wx.EXPAND, 5 )

        bSizer11 = wx.BoxSizer( wx.VERTICAL )


        bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.dlg_credit_button = wx.Button( self, wx.ID_ANY, _(u"Credit"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.dlg_credit_button, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer11, 0, wx.EXPAND, 5 )


        self.SetSizer( bSizer4 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.windows_setting_task_manager_button.Bind( wx.EVT_BUTTON, self.windows_setting_task_manager_button_evnt )
        self.windows_setting_sys_cntrl_button.Bind( wx.EVT_BUTTON, self.windows_setting_sys_cntrl_button_evnt )
        self.windows_setting_perf_rel_button.Bind( wx.EVT_BUTTON, self.windows_setting_perf_rel_button_evnt )
        self.system_setting_bios_button.Bind( wx.EVT_BUTTON, self.system_setting_bios_button_evnt )
        self.dlg_credit_button.Bind( wx.EVT_BUTTON, self.dlg_credit_button_evnt )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def windows_setting_task_manager_button_evnt( self, event ):
        event.Skip()

    def windows_setting_sys_cntrl_button_evnt( self, event ):
        event.Skip()

    def windows_setting_perf_rel_button_evnt( self, event ):
        event.Skip()

    def system_setting_bios_button_evnt( self, event ):
        event.Skip()

    def dlg_credit_button_evnt( self, event ):
        event.Skip()


###########################################################################
## Class Credit
###########################################################################

class Credit ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 309,437 ), style = wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer12 = wx.BoxSizer( wx.VERTICAL )

        self.m_richText1 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, _(u"Hey, you found the credits, congrats. It's just a little school project, but I still wanted to add some credit to it. So hi, I'm Eric from Germany. Here is my link to my GitHub page, so if you are interested, take a peek."), wx.DefaultPosition, wx.Size( 500,90 ), wx.TE_READONLY|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
        bSizer12.Add( self.m_richText1, 0, wx.EXPAND |wx.ALL, 5 )

        self.credit_img = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Pics/ゼロ 零 - 123991796 - カペラ：『頑張ったペットには特別な褒美があるよ〜』 (Klein).png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.credit_img, 0, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer12 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.credit_img.Bind( wx.EVT_LEFT_DOWN, self.bitmap_credit_click )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def bitmap_credit_click( self, event ):
        event.Skip()


