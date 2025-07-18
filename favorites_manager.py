import json
import os

FAV_FILE = "favorites.json"

def load_favorites():
    if not os.path.exists(FAV_FILE):
        return []
    with open(FAV_FILE, "r") as f:
        return json.load(f)

def save_favorites(favorites):
    with open(FAV_FILE, "w") as f:
        json.dump(favorites, f, indent=2)

def add_to_favorites(recipe):
    favorites = load_favorites()
    if recipe not in favorites:
        favorites.append(recipe)
        save_favorites(favorites)

def view_favorites():
    favorites = load_favorites()
    if not favorites:
        print("No favorites yet.")
    else:
        for idx, r in enumerate(favorites, 1):
            print(f"\n{idx}. {r['name']}")
            print("Ingredients:", ", ".join(r["ingredients"]))
            print("Instructions:", r["instructions"])
