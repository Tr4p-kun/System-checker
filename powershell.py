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

