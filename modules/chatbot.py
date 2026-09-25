def gym_buddy_response(message):
    text = message.lower()
    if "missed" in text:
        return "Missing one session is okay. Resume with your next planned session instead of trying to compensate with excessive exercise."
    if "beginner" in text:
        return "Start with simple movements, learn comfortable technique, and increase difficulty gradually."
    if "motivation" in text:
        return "Consistency matters more than a perfect day. Pick one small action and start there."
    if "pain" in text or "injury" in text:
        return "Stop the activity if you have pain or an injury concern and talk to a qualified healthcare professional."
    return "I can help with workout planning, healthy routines, exercise basics, and habit tracking."
