import subprocess



# https://www.phillipsj.net/posts/executing-powershell-from-python/

class runner():
    def __init__(self):
        pass

    def run(self, cmd):
        completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        return completed

    def run_admin(self, cmd): # gemini
        admin_wrapper = f"Start-Process powershell -ArgumentList '-Command {cmd}' -Verb RunAs -Wait"
        return self.run(admin_wrapper)

    def get_uuid(self):
        uuid_getter = self.run("Get-CimInstance Win32_ComputerSystemProduct | Select-Object UUID")
        if uuid_getter.returncode != 0:
            print("An error occured: %s", uuid_getter.stderr)
        else:
            print(uuid_getter.stdout.decode())

    def programm_opener(self, programm, admin=False):
        if admin:
            run_sys_cntrl = self.run_admin(programm)
        else:
            run_sys_cntrl = self.run(programm)
        if run_sys_cntrl.returncode != 0:
            print("An error occured: %s", run_sys_cntrl.stderr)

    def info_collector(self): # powershell load time optimisierung per google gemini hilfe
        get_info = ("Get-CimInstance Win32_Processor | Select-Object -ExpandProperty Name; "
        "Get-CimInstance Win32_Baseboard | Select-Object -ExpandProperty Product; "
        "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name; "
        "(Get-CimInstance Win32_PhysicalMemory | Select-Object -ExpandProperty Devicelocator) -join ','; "
        "(Get-CimInstance Win32_PhysicalMemory | ForEach-Object { $_.Capacity / 1GB }) -join ','; "
        "(Get-CimInstance Win32_PhysicalMemory | Select-Object -ExpandProperty Speed) -join ','; "
        "(Get-CimInstance Win32_LogicalDisk | ForEach-Object { if ($_.VolumeName) { $_.VolumeName } else { $_.DeviceID } }) -join ','; "
        "(Get-CimInstance Win32_LogicalDisk | Select-Object -ExpandProperty Size) -join ','; "
        "(Get-CimInstance Win32_LogicalDisk | Select-Object -ExpandProperty FreeSpace) -join ','; "
        "Get-CimInstance Win32_Processor | Select-Object -ExpandProperty MaxClockSpeed; "
        "Get-CimInstance Win32_Processor | Select-Object -ExpandProperty SocketDesignation")
        result = []
        worker = self.run(get_info)
        if worker.returncode != 0:
            result.append(f"Error: {worker.stderr.decode().strip()}")
        else:
            result = [line.strip() for line in worker.stdout.decode().splitlines() if line.strip()]
        return result


