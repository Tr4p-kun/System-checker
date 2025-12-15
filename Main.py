import platform
import wx
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
        c = wmi.WMI()

    def init_logic(self):
        self.gui_box.SetColLabelValue(0, "Info")
        self.gui_box.SetColLabelValue(1, "Wert")

    def adder(self):
        grid = self.gui_box

        grid.ClearGrid()

        if grid.GetNumberRows() > 0:
            grid.DeleteRows(0, grid.GetNumberRows())

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

def start():
    app = wx.App()
    frm = MainFrame(None)
    frm.Show()
    app.MainLoop()


if __name__ == '__main__':
    start()
