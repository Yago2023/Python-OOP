class Item: 
    pay_rate= 0.8 # the pay rate after 20% discount
    def __init__ (self, name: str, price: float,quantity=0 ): #as I already put =0 quantity is a INT
        # Run valodations to the received arguments
        assert price >= 0, f"Price {price} os not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} os not greater than or equal to zero!"

        # Assign to self object
        self.name = name 
        self.price = price 
        self.quantity = quantity

    def calculate_total_price (self):
        return self.price * self.quantity

    def appply_discount(self):
        self.price = self.price * Item.pay_rate   #diferença entre Item.pay_rate e self.pay_rate

item1 = Item("Phone", 300 , 5)

item2 = Item ("Laptop" , 500 , 3)

item2.has_numpad = False  # add nova instancia 

'''print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)'''


print(Item.__dict__) #All the atributes for Class level
print(item1.__dict__) # All the attributes for instance level / convert it from dictionary 


item1.appply_discount()
#print(item1.price)


item2 = Item ("Laptop" , 500 , 3)
item2.pay_rate = 0.7
item2.appply_discount()
print(item2.price)