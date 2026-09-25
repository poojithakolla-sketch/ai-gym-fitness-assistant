def habit_score(habits):
    if not habits:
        return 0
    return round(sum(bool(v) for v in habits.values()) / len(habits) * 100)

def habit_message(score):
    if score == 100:
        return "All four habits are checked today. Keep the routine consistent."
    if score >= 75:
        return "Good consistency today. Focus on completing the remaining habit."
    if score >= 50:
        return "You have a solid start. Keep the next step small and realistic."
    return "Start with one manageable habit and build consistency gradually."
