import wmi
import platform

import jsonizer
import powershell
from powershell import runner

class Hardware:
    def __init__(self):
        self.standart = [
            ("Archetecture", platform.architecture()[0]),
            ("Machine", platform.machine()),
            ("CPU", powershell.runner.info_collector(self)[0]),
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
            ("CPU", powershell.runner.info_collector(self)[0]),
            ("GPU", powershell.runner.info_collector(self)[2]),
            ("Motherboard", powershell.runner.info_collector(self)[1])
        ]

        self.info_extra = [
            ("Detailed Name", platform.uname()),
            ("Alias", platform.system_alias(platform.system(), platform.release(), platform.version())),
            ("Version", platform.version())
        ]

        self.selected_list = self.standart

class Software:
    def __init__(self):
        self.wmi_process()
        jsonizer.converter.jsoner(self)


    def wmi_process(self):
        c = wmi.WMI()
        process_ids = []

        for process in c.Win32_Process():   # Code von ChatGPT: für umwandel von strings in eine liste
            process_ids.append(process.ProcessId)
        return process_ids











