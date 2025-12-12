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


        self.info_list = [
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
    for process in c.Win32_Process():
        # print(process.ProcessId, process.Name)
        id_list = str(process.ProcessId)
        #print(id_list)
        test = id_list.strip().split("\n")
        for i in test:
            a = []
            a.extend(test)
            print(a)



class MainFrame(GUI.gui_box, Hardware, Software):
    def __init__(self, parent):
        GUI.gui_box.__init__(self, parent)
        Hardware.__init__(self)
        Software.__init__(self)
        # self.init_logic()
        # self.adder()
        c = wmi.WMI()

    # def init_logic(self):
    #     self.gui_list.InsertColumn(0, "Info")
    #     self.gui_list.InsertColumn(1, "Wert")
    #
    # def adder(self):
    #     for i, (prop, val) in enumerate(self.selected_list):    # CHATGPT: Er sollte mir das Hardcoded in eine schleife umwandeln
    #         index = self.gui_list.InsertItem(i, prop)
    #         self.gui_list.SetItem(index, 1, str(val))
    #         print(str(val))
    #
    # def active_standart( self, event ):
    #     self.selected_list = self.standart
    #     self.gui_list.DeleteAllItems()
    #     self.adder()
    #
    # def active_hardware( self, event ):
    #     self.selected_list = self.info_hardware
    #     self.gui_list.DeleteAllItems()
    #     self. adder()
    #
    # def active_windows( self, event ):
    #     self.selected_list = self.info_list
    #     self.gui_list.DeleteAllItems()
    #     self.adder()
    #
    # def active_extra( self, event ):
    #     self.selected_list = self.info_extra
    #     self.gui_list.DeleteAllItems()
    #     self.adder()

def start():
    app = wx.App()
    frm = MainFrame(None)
    frm.Show()
    app.MainLoop()


if __name__ == '__main__':
    start()
