import subprocess

# https://www.phillipsj.net/posts/executing-powershell-from-python/

class runner():
    def __init__(self):
        pass

    def run(self, cmd):
        completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True)
        return completed

    def get_uuid(self):
        uuid_getter = self.run("Get-CimInstance Win32_ComputerSystemProduct | Select-Object UUID")
        if uuid_getter.returncode != 0:
            print("An error occured: %s", uuid_getter.stderr)
        else:
            print(uuid_getter.stdout.decode())

    def open_task_manger(self):
        run_task_manager = self.run("Taskmgr.exe")
        if run_task_manager.returncode != 0:
            print("An error occured: %s", run_task_manager.stderr)


    def open_sys_cntrl(self):
        run_sys_cntrl = self.run("control.exe")
        if run_sys_cntrl.returncode != 0:
            print("An error occured: %s", run_sys_cntrl.stderr)

    def info_collector(self):
        get_info = ["Get-CimInstance Win32_Processor | Select-Object -ExpandProperty Name","Get-CimInstance Win32_Baseboard | Select-Object -ExpandProperty Product","Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"]
        result = []
        for cmd in get_info:
            worker = self.run(cmd)
            if worker.returncode != 0:
                result.append(f"Error: {worker.stderr.decode().strip()}")
            else:
                result.append(worker.stdout.decode().strip())
        return result

# Get-CimInstance Win32_LogicalDisk
#  Get-CimInstance Win32_PhysicalMemory


