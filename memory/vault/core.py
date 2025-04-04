import json
import os

class Vault:
    def __init__(self, path="vault_store.json"):
        self.path = path
        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({}, f)

    def store(self, key, value):
        data = self._load()
        data[key] = value
        self._save(data)
        return f"Stored {key}"

    def retrieve(self, key):
        data = self._load()
        return data.get(key, None)

    def _load(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)