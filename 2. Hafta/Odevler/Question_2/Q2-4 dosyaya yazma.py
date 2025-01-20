import json

def save_to_file(collection, filename="movies.json"):
    with open(filename, "w") as file:
        json.dump(collection, file)
    print("Movies saved to file!")

def load_from_file(filename="movies.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved data found. Starting with an empty collection.")
        return []
