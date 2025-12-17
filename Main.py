import wx
import wx.aui
import GUI
import python_read
import powershell

class MainFrame(GUI.gui_box, python_read.Hardware, python_read.Software):
    def __init__(self, parent):
        GUI.gui_box.__init__(self, parent)
        python_read.Hardware.__init__(self)
        python_read.Software.__init__(self)
        self.init_logic()
        self.adder()
        self.initializer = 0

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

    def activate_window_button_switch( self, event ):
        self.initializer += 1   # gemini switch case code
        switch_rule = self.initializer % 5 # größere zahl größere switch case
        switch_rule += 1
        print(switch_rule)
        match switch_rule:
            case 1:
                self.gui_box.SetColLabelValue(0, "Info")
                self.gui_box.SetColLabelValue(1, "Wert")
                self.gui_box.Layout()
                self.Layout()
            case 2:
                self.gui_box.SetColLabelValue(0, "PID")
                self.gui_box.SetColLabelValue(1, "Name")
                self.gui_box.Layout()
                self.Layout()
            case 3:
                print("3")



def start():
    app = wx.App()
    frm = MainFrame(None)
    frm.Show()
    app.MainLoop()



if __name__ == '__main__':
    start()
