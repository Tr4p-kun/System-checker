import wmi
import platform
import jsonizer
import powershell



class Hardware:
    def __init__(self, ps_runner):
        self.ps_runner = ps_runner

        def clean_powershell_output(raw_text, separator=", "):  #Gemini code
            if not raw_text:
                return ""

            clean_list = [line.strip() for line in raw_text.splitlines() if line.strip()]

            return separator.join(clean_list)

        daten_paket = self.ps_runner.info_collector()

        hard_drive_size_worker = clean_powershell_output(daten_paket[7], separator=",")
        total_size_int = sum(int(zahl) for zahl in hard_drive_size_worker.split(","))
        convert_to_GB_size = total_size_int / (1024**3)
        convert_to_GB_size_rounded = round(convert_to_GB_size, 2)

        hard_drive_freespace_worker = clean_powershell_output(daten_paket[8])
        total_free_int = sum(int(zahl) for zahl in hard_drive_freespace_worker.split(","))
        convert_to_GB_free = total_free_int / (1024**3)
        convert_to_GB_free_rounded = round(convert_to_GB_free, 2)

        self._standart = [
            ("Architecture", platform.architecture()[0]),
            ("Machine", platform.machine()),
            ("CPU", daten_paket[0]),
            ("PC Name", platform.node()),
            ("System", platform.system()),
            ("Release", platform.release()),
            ("Win Version", platform.win32_ver()[1:3]),
            ("Win Edition", platform.win32_edition()),
        ]


        self._info_windows = [
            ("PC Name", platform.node()),
            ("System", platform.system()),
            ("Release", platform.release()),
            ("Win Version", platform.win32_ver()[1:3]),
            ("Win Edition", platform.win32_edition()),

        ]



        self._info_hardware = [
            ("Machine", platform.machine()),
            ("Architecture", platform.architecture()[0]),
            ("Motherboard", daten_paket[1]),
            ("CPU Name", daten_paket[0]),
            ("CPU Speed", daten_paket[9]),
            ("CPU Socket", daten_paket[10]),
            ("GPU", daten_paket[2]),
            ("RAM Slots", clean_powershell_output(daten_paket[3])),
            ("RAM Capacity", clean_powershell_output(daten_paket[4])),
            ("Ram Speed", clean_powershell_output(daten_paket[5])),
            ("Hard Drive", clean_powershell_output(daten_paket[6])),
            ("Hard Drive Size", f"{convert_to_GB_size_rounded} GB"),
            ("Hard Drive Free Space", f"{convert_to_GB_free_rounded} GB" )

        ]

        self._info_extra = [
            ("Detailed Name", platform.uname()),
            ("Alias", platform.system_alias(platform.system(), platform.release(), platform.version())),
            ("Version", platform.version())
        ]

        self.selected_list = self.get_standart()

    def get_standart(self):
        return self._standart

    def get_info_windows(self):
        return self._info_windows

    def get_info_hardware(self):
        return self._info_hardware

    def get_info_extra(self):
        return self._info_extra


class Software:
    def __init__(self):
        self.wmi_process()
        jsonizer.converter.jsoner(self)


    # def wmi_process(self):
    #     c = wmi.WMI()
    #     process_ids = []
    #
    #     for process in c.Win32_Process():   # Code von ChatGPT: für umwandel von strings in eine liste
    #         process_ids.append(process.ProcessId)
    #     return process_ids











