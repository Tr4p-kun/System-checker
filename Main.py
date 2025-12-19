import wx
import wx.aui
import GUI
import python_read
import powershell

class MainFrame(GUI.gui_box, python_read.Hardware, python_read.Software, powershell.runner):
    def __init__(self, parent):
        GUI.gui_box.__init__(self, parent)
        python_read.Hardware.__init__(self)
        python_read.Software.__init__(self)
        powershell.runner.__init__(self)
        self.init_logic()
        self.adder()
        self.initializer = 0
        powershell.runner.get_uuid(self) # TODO für denn jsonizer nutzen

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

    def activate_task_mngr_men( self, event ):
        self.gui_box.SetColLabelValue(0, "PID")
        self.gui_box.SetColLabelValue(1, "Name")
        self.gui_box.DeleteRows(0, self.gui_box.GetNumberRows())
        self.gui_box.AppendRows(len(python_read.Software.wmi_process(self)))
        self.gui_box.Layout()
        self.Layout()

    def activate_task_mngr_win_men( self, event ):
        powershell.runner.open_task_manger(self)

    def activate_sys_cntr_men( self, event ):



def start():
    app = wx.App()
    frm = MainFrame(None)
    frm.Show()
    app.MainLoop()



if __name__ == '__main__':
    start()
