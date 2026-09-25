def nutrition_guidance(goal, preference):
    base = {
        "Breakfast": ["Oats or whole-grain breakfast", "Fruit", "A protein source such as eggs, curd, tofu or beans"],
        "Lunch": ["Rice/roti or another whole grain", "Vegetables", "Dal/beans/tofu/egg or another protein source"],
        "Snack": ["Fruit", "Nuts/seeds or yogurt/curd"],
        "Dinner": ["Vegetables", "A grain/starch", "A protein source"],
    }
    if preference == "Vegetarian":
        base["Breakfast"][-1] = "Curd, paneer, tofu or another vegetarian protein source"
        base["Lunch"][-1] = "Dal, beans, paneer or tofu"
    elif preference == "Vegan":
        base["Breakfast"][-1] = "Soy milk, tofu, beans or another plant protein"
        base["Lunch"][-1] = "Dal, beans, chickpeas or tofu"
    elif preference == "High-protein":
        base["Breakfast"].append("Add a protein-rich food appropriate for you")
        base["Lunch"].append("Include a substantial protein source")
    return base
