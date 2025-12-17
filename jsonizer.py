import json
import python_read

# https://codeinstitute.net/de/blog/working-with-json-in-python/

class converter:
    def __init__(self):
        self.jsoner()

    def jsoner(self):
        x = {"process_ids": python_read.Software.wmi_process(self)}
        with open('test.json', 'w') as file:
            json.dump(x, file)

