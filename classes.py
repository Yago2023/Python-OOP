class Item: #molde para criar objetos
    def calculate_total_price(self,x,y): #metodo
        return x * y
    

item1 = Item()  #criando um objeto
item1.name="phone" #atribuições a objetos / instancias da classe 
item1.price= 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price,item1.quantity))
