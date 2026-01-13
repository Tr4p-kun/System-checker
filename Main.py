import wx
import wx.aui
import GUI
import python_read
import powershell
import time

start_time = time.time()



class MainFrame(GUI.gui_box, python_read.Hardware, python_read.Software, powershell.runner):
    def __init__(self, parent):
        GUI.gui_box.__init__(self, parent)
        python_read.Hardware.__init__(self)
        # python_read.Software.__init__(self)
        powershell.runner.__init__(self)
        self.init_logic()
        self.adder()
        self.initializer = 0
        #powershell.runner.get_uuid(self) # TODO für denn jsonizer nutzen

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

    # def activate_task_mngr_men( self, event ):
    #     self.gui_box.SetColLabelValue(0, "PID")
    #     self.gui_box.SetColLabelValue(1, "Name")
    #     self.gui_box.DeleteRows(0, self.gui_box.GetNumberRows())
    #     self.gui_box.AppendRows(len(python_read.Software.wmi_process(self)))
    #     self.gui_box.Layout()
    #     self.Layout()

    def main_button_open_panel_settings_evnt(self, event):
        dlg = Setting_Dlg(parent=self)
        dlg.ShowModal()

class Setting_Dlg(GUI.Settings_Dlg, powershell.runner):
    def __init__(self, parent):
        GUI.Settings_Dlg.__init__(self, parent)


    def windows_setting_task_manager_button_evnt( self, event ):
        powershell.runner.programm_opener(self, "Taskmgr.exe", admin=False)

    def windows_setting_sys_cntrl_button_evnt( self, event ):
        powershell.runner.programm_opener(self, "control.exe", admin=False)

    def windows_setting_perf_rel_button_evnt( self, event ):
        powershell.runner.programm_opener(self, "perfmon.exe /rel", admin=False)

    def system_setting_bios_button_evnt( self, event ):
        #powershell.runner.programm_opener(self, "shutdown.exe /r /fw /t 1", admin=True)
        powershell.runner.programm_opener(self, "Set-Content -Path $env:USERPROFILE\\Desktop\\admin_test.txt -Value Admin-Erfolg", admin=True)



def start():
    app = wx.App()
    frm = MainFrame(None)
    frm.Show()
    end_time = time.time()
    duration = end_time - start_time
    print(duration)
    app.MainLoop()



if __name__ == '__main__':
    start()
