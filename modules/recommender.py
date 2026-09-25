def recommend_workouts(goal, experience, days):
    templates = {
        "General fitness": ["Full body", "Cardio", "Mobility", "Full body", "Active recovery", "Cardio", "Rest"],
        "Strength": ["Full body strength", "Mobility", "Upper body", "Rest", "Lower body", "Full body strength", "Rest"],
        "Endurance": ["Easy cardio", "Mobility", "Intervals", "Rest", "Easy cardio", "Longer cardio", "Rest"],
        "Mobility": ["Mobility", "Light cardio", "Mobility", "Rest", "Mobility", "Light full body", "Rest"],
    }
    items = templates.get(goal, templates["General fitness"])[:days]
    return [{"Day": i + 1, "Plan": plan, "Level": experience} for i, plan in enumerate(items)]
