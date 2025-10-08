class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self._quantity = quantity

    def get_quantity(self):
        return self._quantity
    
    def update_quantity(self, amount: int):
        return self._quantity + amount
    
    def calculate_total_value(self):
        return self.price * self._quantity
    
    def __str__(self):
        return f"Product #{self.product_id} -- {self.name} -- {self._quantity}"
    

class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, quantity, warranty_period, power_consumption):
        super().__init__(product_id, name, price, quantity)
        self.warranty_period = warranty_period
        self.power_consumption = power_consumption

    def __str__(self):
        return f"Product #{self.product_id} -- {self.name} -- {self._quantity} -- {self.power_consumption} -- {self.warranty_period}"
    

class ClothingProduct(Product):
    def __init__(self, product_id, name, price, quantity, size, material, color):
        super().__init__(product_id, name, price, quantity)
        self.size = size
        self.material = material
        self.color = color

    def __str__(self):
        return f"Product #{self.product_id} -- {self.name} -- {self.color} -- {self.material} -- {self.size} {self._quantity}"
    

class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        self._products[product.product_id] = product
        return f"Product #{product.product_id} has been added successfully"
    
    def remove_product(self, product_id):
        if product_id in self._products:
            self._products.pop(product_id)
            return True
        return False 
    
    def list_all_products(self):
        for value in self._products.values():
            print(value)
    


inventory = Inventory()
    
# Add products
inventory.add_product(ElectronicProduct("E001", "Smartphone", 699.99, 50, 24, "5W"))
inventory.add_product(ElectronicProduct("E002", "Laptop", 1299.99, 25, 36, "65W"))
inventory.add_product(ClothingProduct("C001", "T-Shirt", 29.99, 100, "M", "Cotton", "Blue"))
inventory.add_product(ClothingProduct("C002", "Jeans", 59.99, 75, "L", "Denim", "Black"))

# List all products
print("All Products:")
inventory.list_all_products()
        
        