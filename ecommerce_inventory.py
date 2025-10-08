from functools import reduce

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self._quantity = quantity

    def get_quantity(self):
        return self._quantity
    
    def update_quantity(self, amount: int):
        self._quantity = self._quantity + amount
    
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
    
    def find_product(self, product_id):
        return self._products.get(product_id)
    
    def get_low_stock_products(self, threshold):
        return [product.name for product in self._products.values() if product.get_quantity() < threshold]
       
    def calculate_total_inventory_value(self):
        return reduce((lambda acc, curr: acc + curr.calculate_total_value()), self._products.values(), 0)

    def apply_discount(self, product_id, percentage):
        if product_id in self._products:
            product = self._products[product_id]
            discount_amount = product.price * (percentage / 100)
            product.price -= discount_amount
            return f"Applied {percentage}% discount to {product.name}"
        return f"Product {product_id} not found"
    
    def list_all_products(self):
        for value in self._products.values():
            print(value)
    
from functools import reduce

# Your existing classes here (copy all your class definitions)

# COMPREHENSIVE TEST
def test_inventory_system():
    print("=" * 50)
    print("COMPREHENSIVE INVENTORY SYSTEM TEST")
    print("=" * 50)
    
    inventory = Inventory()
    
    # Test 1: Adding Products
    print("\n1. TESTING ADD PRODUCTS:")
    print("-" * 30)
    print(inventory.add_product(ElectronicProduct("E001", "Smartphone", 699.99, 50, 24, "5W")))
    print(inventory.add_product(ElectronicProduct("E002", "Laptop", 1299.99, 25, 36, "65W")))
    print(inventory.add_product(ClothingProduct("C001", "T-Shirt", 29.99, 100, "M", "Cotton", "Blue")))
    print(inventory.add_product(ClothingProduct("C002", "Jeans", 59.99, 75, "L", "Denim", "Black")))
    
    # Test 2: List All Products
    print("\n2. LISTING ALL PRODUCTS:")
    print("-" * 30)
    inventory.list_all_products()
    
    # Test 3: Calculate Total Inventory Value
    print("\n3. CALCULATING TOTAL INVENTORY VALUE:")
    print("-" * 30)
    total_value = inventory.calculate_total_inventory_value()
    print(f"Total Inventory Value: ${total_value:.2f}")
    
    # Test 4: Find Low Stock Products
    print("\n4. FINDING LOW STOCK PRODUCTS:")
    print("-" * 30)
    low_stock_30 = inventory.get_low_stock_products(30)
    print(f"Products with less than 30 stock: {[p for p in low_stock_30]}")
    
    low_stock_80 = inventory.get_low_stock_products(80)
    print(f"Products with less than 80 stock: {[p for p in low_stock_80]}")
    
    # Test 5: Find Specific Products
    print("\n5. FINDING SPECIFIC PRODUCTS:")
    print("-" * 30)
    found_product = inventory.find_product("E001")
    print(f"Found product E001: {found_product.name if found_product else 'Not found'}")
    
    not_found = inventory.find_product("E999")
    print(f"Found product E999: {'Found' if not_found else 'Not found'}")
    
    # Test 6: Apply Discounts
    print("\n6. APPLYING DISCOUNTS:")
    print("-" * 30)
    print(inventory.apply_discount("C001", 20))  # 20% discount on T-Shirt
    print(inventory.apply_discount("E999", 10))  # Try discount on non-existent product
    
    # Check price after discount
    tshirt = inventory.find_product("C001")
    print(f"T-Shirt price after discount: ${tshirt.price:.2f}")
    
    # Test 7: Update Quantities
    print("\n7. UPDATING QUANTITIES:")
    print("-" * 30)
    laptop = inventory.find_product("E002")
    print(f"Laptop quantity before: {laptop.get_quantity()}")
    laptop.update_quantity(10)  # Add 10 more laptops
    print(f"Laptop quantity after adding 10: {laptop.get_quantity()}")
    
    laptop.update_quantity(-5)  # Sell 5 laptops
    print(f"Laptop quantity after selling 5: {laptop.get_quantity()}")
    
    # Test 8: Calculate Individual Product Values
    print("\n8. CALCULATING INDIVIDUAL PRODUCT VALUES:")
    print("-" * 30)
    for product_id, product in inventory._products.items():
        product_value = product.calculate_total_value()
        print(f"{product.name}: ${product_value:.2f}")
    
    # Test 9: Remove Product
    print("\n9. REMOVING A PRODUCT:")
    print("-" * 30)
    print(f"Removing product C002: {inventory.remove_product('C002')}")
    print(f"Removing non-existent product XYZ: {inventory.remove_product('XYZ')}")
    
    # Test 10: Final State
    print("\n10. FINAL INVENTORY STATE:")
    print("-" * 30)
    inventory.list_all_products()
    
    final_total = inventory.calculate_total_inventory_value()
    print(f"Final Total Inventory Value: ${final_total:.2f}")
    
    # Test 11: Test Inheritance and Polymorphism
    print("\n11. TESTING INHERITANCE AND POLYMORPHISM:")
    print("-" * 30)
    for product in inventory._products.values():
        print(f"Type: {type(product).__name__}")
        print(f"Calculate Total Value: ${product.calculate_total_value():.2f}")
        print(f"String representation: {product}")
        print("-" * 20)
    
    print("=" * 50)
    print("ALL TESTS COMPLETED! ✅")
    print("=" * 50)

# Run the comprehensive test
if __name__ == "__main__":
    test_inventory_system()