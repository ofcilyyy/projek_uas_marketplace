class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_details(self):
        return f"ID: {self.product_id} | {self.name} - Rp{self.price:,}"
