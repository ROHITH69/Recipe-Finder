from recipe_searcher import search_recipes
from favorites_manager import add_to_favorites, view_favorites
import json

def load_data():
    with open("data.json", "r") as f:
        return json.load(f)

def main():
    recipes = load_data()
    while True:
        print("\n=== Recipe Finder ===")
        print("1. Search Recipes")
        print("2. View Favorites")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            keyword = input("Enter ingredient or recipe name to search: ")
            results = search_recipes(recipes, keyword)
            if results:
                for idx, r in enumerate(results, 1):
                    print(f"\n{idx}. {r['name']}")
                    print("Ingredients:", ", ".join(r["ingredients"]))
                    print("Instructions:", r["instructions"])
                fav = input("\nDo you want to add any recipe to favorites? (yes/no): ")
                if fav.lower() == "yes":
                    index = int(input("Enter the number of the recipe: ")) - 1
                    if 0 <= index < len(results):
                        add_to_favorites(results[index])
                        print("Added to favorites.")
            else:
                print("No recipes found.")
        elif choice == "2":
            view_favorites()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
