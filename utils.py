def format_recipe(recipe):
    return (
        f"🍲 Recipe Name: {recipe['name']}\n"
        f"🕒 Time: {recipe['cook_time']} mins\n"
        f"📋 Ingredients: {', '.join(recipe['ingredients'])}\n"
        f"📖 Instructions: {recipe['instructions']}\n"
    )
