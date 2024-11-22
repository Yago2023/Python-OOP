class Item: 
    def __init__ (self, name: str, price: float,quantidy=0 ): #as I already put =0 quantity is a INT
        # Run valodations to the received arguments
        assert price >= 0, f"Price {price} os not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantidy} os not greater than or equal to zero!"

        # Assign to self object
        self.name = name 
        self.price = price 
        self.quantidy = quantity

    def calculate_total_price (self):
        return self.price * self.quantity


item1 = Item("Phone", 300 , 5)

item2 = Item ("Laptop" , 500 , 3)

item2.has_numpad = False  # add nova instancia 

print(item1.calculate_total_price())