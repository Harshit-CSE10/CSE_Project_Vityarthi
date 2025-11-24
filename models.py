class Product:
    """
    Represents a single inventory item.
    """
    def __init__(self, product_id, name, price, quantity, threshold=5):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.threshold = threshold

    def to_dict(self):
        #Converts object to dictionary for JSON storage.#
        return {
            "id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "threshold": self.threshold
        }

    @staticmethod
    def from_dict(data):
        """Creates a Product object from a dictionary."""
        return Product(data['id'], data['name'], data['price'], data['quantity'], data['threshold'])