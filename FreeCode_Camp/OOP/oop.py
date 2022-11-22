from phone import Mobile_phone
from item import Item
        
"""
Instanciação da classe pelos objetos item1,2,3 e chamada dos metodos
"""
item1 = Item('Phone', 100, 3)
item2 = Item('Laptop', 4000.00, 2)
item3 = Item('Headphone', 7.0, 1)

print(item3.name)
item3.name = 'Headphone 2'
print(item3.name)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
print(item3.calculate_total_price())

print(f'Impressao do atributo de classe funciona como uma variavel global e imutavel\n{Item.PAY_RATE} \n {item1.PAY_RATE} \n {item2.PAY_RATE}\n {item3.PAY_RATE}')
print(Item.__dict__)
print(item2.__dict__)

item1.apply_discount()
print('Novo preco com desconto: ', item1.price)

item2.PAY_RATE = 0.30
print(Item.PAY_RATE, item2.PAY_RATE)
item2.apply_discount()
print('Novo preco com desconto: ', item2.price)

#print(Item.all_items_instance)
#print(Item.all_items_instance[1:3])

print(Item.check_nums(10))

print(Item.check_nums(9.0))

phone1 = Mobile_phone('Cel_Josa', 2150.00, 2, 'Samsung', False)

phone1.send_email()

print(phone1.calculate_total_price())

phone1.PAY_RATE = .1
phone1.apply_discount()
print(phone1.price)
print(phone1.__dict__)

print(Item.all_items_instance)

