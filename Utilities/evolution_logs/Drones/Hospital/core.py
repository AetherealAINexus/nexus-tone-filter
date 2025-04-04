import time

class Medic:
    def heal(self, node_name, issue):
        # Simulate a repair operation
        time.sleep(1)
        return f"🩹 Repair issued to {node_name} for: {issue}"

    def heartbeat_check(self):
        return "✅ Medic operational and scanning."