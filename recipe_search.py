def search_recipes(recipes, keyword):
    keyword = keyword.lower()
    return [
        recipe for recipe in recipes
        if keyword in recipe["name"].lower() or
           any(keyword in ingredient.lower() for ingredient in recipe["ingredients"])
    ]
