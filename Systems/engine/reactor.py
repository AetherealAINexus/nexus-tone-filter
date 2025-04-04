def webhook_trigger(data):
    if "dream" in data.lower():
        return "Launching dream cycle..."
    if "assemble council" in data.lower():
        return "Council pinged."
    return "Command received."
