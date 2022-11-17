class Item:
    """
    Usar os tipos dos argumentos como no exemplo abaixo para forçar os tipos de parametros a serem especificados
    assert para validar os argumentos recebidos como parametros
    """
    PAY_RATE = 0.8
    all_items_instance = []

    def __init__(self, name: str, price: float, quantity=0) -> None:
        """
        Pesquisar melhor como reforçar o tipo, 
        gerando um erro no momento de passagem dos parametros para os argumentos do metodo
        Pois aqui nao funcionou eu convertendo preco e qtd para String
        """

        #garantir que os valores sejam sempre igual ou maior que 0
        assert price >=0 , f'Preco {price} e um valor negativo'
        assert quantity >=0 , f'Quantidade {quantity} e um valor negativo'

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all_items_instance.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        """
        Excelente exemplo aqui sobre Heranca de atributos, pois uma vez que antes estava com o pay_rate da classe e nao da instancia
        Independente de termos designado o valor diferente no nivel da instancia, o valor do disconto era considerando o valor da Classe
        Sendo assim nesse caso em especifico, o melhor é mesmo manter o self, pois no caso de nao haver nenhuma nova atribuicao para a variavel no nivel da instancia,
        ela pega automaticamente por Heranca o valor atribuido no nível da Classe
        """
        self.price = self.price * self.PAY_RATE #Item.PAY_RATE

    def __repr__(self) -> str:
        return f'Item({self.name}, {self.price}, {self.quantity})'

item1 = Item('Phone', 100, 3)
item2 = Item('Laptop', 4000.00, 2)
item3 = Item('Headphone', 7.0, 1)

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

print(Item.all_items_instance)
print(Item.all_items_instance[0])