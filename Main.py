import platform
import wx
import wx.aui
import GUI
import wmi

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
    def __init__(self):
        self.test()


    def wmi_process(self):
        c = wmi.WMI()
        process_ids = []

        for process in c.Win32_Process():   # Code von ChatGPT: für umwandel von strings in eine liste
            process_ids.append(process.ProcessId)

        # print(len(process_ids))
        # print(process_ids)
        return process_ids

    def test(self):
        # print(self.wmi_process())
        pass








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

    def resize(self):
        dsize = []
        dsize = self.GetSize()
        self.gui_box.SetColSize(0, ((dsize[0] // 2) - 5)- 50)
        self.gui_box.SetColSize(1, (dsize[0] // 2) - 50)
        self.gui_box.Layout()
        self.Layout()

    def activate_window_size( self, event ):
        if self.IsMaximized() == True:
            self.resize()
        else:
            self.resize()

    def switch_rule(self):
        switcher = 0 # TODO
        switcher += 1
        return switcher

    def activate_window_button_switch( self, event ):
        switcher = self.switch_rule()
        print(switcher)
        if switcher == 1:
            self.gui_box.SetColLabelValue(0, "PID")
            self.gui_box.SetColLabelValue(1, "Name")
            self.gui_box.Layout()
            self.Layout()
        elif switcher == 2:
            print("hello")


def start():
    app = wx.App()
    frm = MainFrame(None)
    frm.Show()
    app.MainLoop()



if __name__ == '__main__':
    start()
