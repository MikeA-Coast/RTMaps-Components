import rtmaps.core as rt
import rtmaps.types
from rtmaps.base_component import BaseComponent
from datetime import datetime
import os

class rtmaps_python(BaseComponent):
    def __init__(self):
        BaseComponent.__init__(self)

    def Dynamic(self):
        self.add_input("in", rtmaps.types.ANY)
        self.add_output("out", rtmaps.types.AUTO)

    def Birth(self):
        print("STARTING TO LOG DATA!!")

        log_dir = r"C:\Users\user\Documents\supervision_logs"
        os.makedirs(log_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.filename = os.path.join(log_dir, f"supervision_log_{timestamp}.txt")

    def Core(self):
        ioelt = self.inputs["in"].ioelt
        raw = ioelt.data

        # Convert numpy array or list of ints to string
        if hasattr(raw, "tolist"):  # handles numpy arrays
            raw = raw.tolist()
        if isinstance(raw, list) and all(isinstance(x, int) for x in raw):
            raw = ''.join(chr(x) for x in raw)

        print("📥 RAW DATA RECEIVED FROM SUPERVISION:\n", raw)


        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(raw.strip() + "\n")

    def Death(self):
        print("......STOPPING NO MORE DATA LOGGING :)")
