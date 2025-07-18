from recipe_search import find_recipes
from recipe_data import load_recipes
from utils import format_recipe

def main():
    recipes = load_recipes()
    ingredients = input("Enter ingredients (comma-separated): ").lower().split(',')

    results = find_recipes(recipes, ingredients)

    if results:
        print("\n🍽️ Recipes Found:\n")
        for recipe in results:
            print(format_recipe(recipe))
            print("-" * 40)
    else:
        print("\n❌ No matching recipes found.")

if __name__ == "__main__":
    main()
