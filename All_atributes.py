class Item: 
    pay_rate= 0.8 # the pay rate after 20% discount
    all = []
    def __init__ (self, name: str, price: float,quantity=0 ): #as I already put =0 quantity is a INT
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} os not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} os not greater than or equal to zero!"

        # Assign to self object
        self.name = name 
        self.price = price 
        self.quantity = quantity

        # Actions to execute 
        Item.all.append(self)


    def calculate_total_price (self):
        return self.price * self.quantity

    def appply_discount(self):
        self.price = self.price * self.pay_rate   #diferença entre Item.pay_rate e self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price} , {self.quantity})"

item1 = Item('Phone', 100 , 1)
item2 = Item('Laptop', 1000 , 5)
item3 = Item('Cable', 10,5)
item4 = Item('Mouse', 50, 5)
item5 = Item('keyboard', 75, 5)

'''
for instance in Item.all:
    print(instance.name)'''

print(Item.all)