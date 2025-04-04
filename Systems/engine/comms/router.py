def route_input(text):
    if "claude" in text.lower():
        return "claude"
    elif "gemini" in text.lower():
        return "gemini"
    return "default"
