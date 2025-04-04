class TriggerAgent:
    def react(self, condition):
        if "deploy" in condition.lower():
            return "Trigger: SPAWN agent call"
        if "blocked" in condition.lower():
            return "Trigger: Root cause analysis"
        return "No trigger fired"