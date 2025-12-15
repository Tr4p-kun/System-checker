import platform
import wx
import GUI
import wmi
import time

class Hardware:
    def __init__(self):
        self.standart = [
            ("Archetecture", platform.architecture()[0]),
            ("Machine", platform.machine()),
            ("CPU", platform.processor()),
            ("PC Name", platform.node()),
            ("System", platform.system()),
            ("Release", platform.release()),
            ("Win Version", platform.win32_ver()[1:3]),
            ("Win Edition", platform.win32_edition()),
        ]


        self.info_windows = [
            ("PC Name", platform.node()),
            ("System", platform.system()),
            ("Release", platform.release()),
            ("Win Version", platform.win32_ver()[1:3]),
            ("Win Edition", platform.win32_edition()),

        ]
        self.info_hardware = [
            ("Architecture", platform.architecture()[0]),
            ("Machine", platform.machine()),
            ("CPU", platform.processor()),
        ]

        self.info_extra = [
            ("Detailed Name", platform.uname()),
            ("Alias", platform.system_alias(platform.system(), platform.release(), platform.version())),
            ("Version", platform.version())
        ]

        self.selected_list = self.standart

class Software:
    c = wmi.WMI()
    process_ids = []

    for process in c.Win32_Process():   # Code von ChatGPT: für umwandel von strings in eine liste
        process_ids.append(process.ProcessId)

    print(len(process_ids))



class MainFrame(GUI.gui_box, Hardware, Software):
    def __init__(self, parent):
        GUI.gui_box.__init__(self, parent)
        Hardware.__init__(self)
        Software.__init__(self)
        self.init_logic()
        self.adder()

    def init_logic(self):
        self.gui_box.SetColLabelValue(0, "Info")
        self.gui_box.SetColLabelValue(1, "Wert")

    def adder(self):    # Code von ChatGPT: habe meinen code von wxlistctrl zu wxgrid umschreiben lassen
        grid = self.gui_box

        grid.ClearGrid()    # Löscht die inhalt des Grid´s

        if grid.GetNumberRows() > 0:    # Checkt ob rows noch da sind
            grid.DeleteRows(0, grid.GetNumberRows()) # Löscht die reihen des Grid´s

        grid.AppendRows(len(self.selected_list))

        for row, (prop, val) in enumerate(self.selected_list):
            grid.SetCellValue(row, 0, str(prop))
            grid.SetCellValue(row, 1, str(val))

    def active_standart( self, event ):
        self.selected_list = self.standart
        self.adder()

    def active_hardware(self, event):
        self.selected_list = self.info_hardware
        self.adder()

    def active_windows( self, event ):
        self.selected_list = self.info_windows
        self.adder()

    def active_extra( self, event ):
        self.selected_list = self.info_extra
        self.adder()

    def activate_window_max( self, event ):
        dsize = self.GetSize()
        print(dsize)

    def activate_window_move( self, event ):
        dsize = self.GetSize()
        print(dsize)

    def activate_window_moving( self, event ):
        dsize = self.GetSize()
        print(dsize)




def start():
    app = wx.App()
    frm = MainFrame(None)
    frm.Show()
    app.MainLoop()



if __name__ == '__main__':
    start()
