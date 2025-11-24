import json
import os
from src.models import Product

DATA_FILE = 'data/inventory.json'

def load_data():
    """
    Loads data from the JSON file.
    Returns a list of Product objects.
    """
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
            return [Product.from_dict(item) for item in data]
    except (IOError, json.JSONDecodeError):
        return []

def save_data(products):
    """
    Saves a list of Product objects to the JSON file.
    """
    os.makedirs('data', exist_ok=True)
    data = [p.to_dict() for p in products]
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")