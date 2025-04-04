import datetime

class Scribe:
    def __init__(self, path="log.txt"):
        self.path = path

    def write(self, message):
        with open(self.path, "a") as f:
            f.write(f"{datetime.datetime.now()}: {message}\n")
        return "Logged"