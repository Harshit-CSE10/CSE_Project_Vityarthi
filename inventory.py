from src.storage import load_data, save_data
from src.models import Product

def get_all_products():
    return load_data()

def add_product(product_id, name, price, quantity):
    """
    Functional Module 1: Add new inventory items.
    """
    products = get_all_products()
    if any(p.product_id == product_id for p in products):
        return False, "Error: Product ID already exists."
    
    new_product = Product(product_id, name, price, quantity)
    products.append(new_product)
    save_data(products)
    return True, "Product added successfully."

def update_stock(product_id, quantity_sold):
    """
    Functional Module 2: Record sales and update stock.
    """
    products = get_all_products()
    for p in products:
        if p.product_id == product_id:
            if p.quantity >= quantity_sold:
                p.quantity -= quantity_sold
                save_data(products)
                return True, f"Sold {quantity_sold} units. Remaining: {p.quantity}"
            else:
                return False, f"Error: Insufficient stock. Only {p.quantity} available."
    return False, "Error: Product ID not found."