def find_recipes(recipes, ingredients):
    matching = []

    for recipe in recipes:
        if all(ing.strip() in map(str.lower, recipe["ingredients"]) for ing in ingredients):
            matching.append(recipe)

    return matching
