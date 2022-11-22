import csv

class Item:
    """
    Usar os tipos dos argumentos como no exemplo abaixo para forçar os tipos de parametros a serem especificados
    assert para validar os argumentos recebidos como parametros
    """
    PAY_RATE = 0.8
    all_items_instance = []

    def __init__(self, name: str, price: float, quantity: int=0) -> None:
        """
        Pesquisar melhor como reforçar o tipo, 
        gerando um erro no momento de passagem dos parametros para os argumentos do metodo
        Pois aqui nao funcionou eu convertendo preco e qtd para String
        """

        #garantir que os valores sejam sempre igual ou maior que 0
        assert price >=0 , f'Preco {price} e um valor negativo'
        assert quantity >=0 , f'Quantidade {quantity} e um valor negativo'

        # __ funciona como declarar o metodo como private, so acessivel de dentro da classe, para isso tem de se definir o decorator @property que significa read-only
        # O atributo fica só sendo acessível no momento de instanciação da classe, ou através do metódo Set que usa-se o decorator @nome_da_variavel.setter, 
        # o que nesse caso fica sendo o proprio name, declaro como privado com o __name no init da classe, depois um metodo @property retornando o __name
        # e depois o decorator @name.setter para definir o valor de __name com argumento passado. DETALHE porque o property e o setter tem que ter o mesmo nome da variavel
        # Excelente para fazer validação de instancia, e demais parametros da classe para garantir a integridade dos objetos e dados da instancia.
        # Isso é a encapsulação

        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all_items_instance.append(self)
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


    def calculate_total_price(self) -> float:
        return self.price * self.quantity
    
    def apply_discount(self) -> None:
        """
        Excelente exemplo aqui sobre Heranca de atributos, pois uma vez que antes estava com o pay_rate da classe e nao da instancia
        Independente de termos designado o valor diferente no nivel da instancia, o valor do disconto era considerando o valor da Classe
        Sendo assim nesse caso em especifico, o melhor é mesmo manter o self, pois no caso de nao haver nenhuma nova atribuicao para a variavel no nivel da instancia,
        ela pega automaticamente por Heranca o valor atribuido no nível da Classe
        """
        self.price = self.price * self.PAY_RATE #Item.PAY_RATE

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: ({self.name}, {self.price}, {self.quantity})'

    def enforce_type_hints(text: str, nrA: int, nrB: int) -> bool:
        if isinstance(int, [nrA, nrB]):
            print(f'Texto enviado como parametro {text}\nSoma dos valores enviados{nrA + nrB}')
        else:
            print('Os numeros enviados nao sao numeros inteiros')
            return False
        return True

    @classmethod
    def instantiate_from_csv(cls, csv_path: str):
        """
        Metodos de classe, são metodos acessiveis a nivel da classe, nesse exemplo, estamos usando para instanciar
        objetos da propria classe a partir de um arquivo CSV que contem os itens que foram criados manualmente nos
        exemplos e codigos abaixo.

        O ponto principal é utilizar o decorator @classmethod, e depois utilizar toda a logica, aqui eu coloquei o parametro
        csv_path apenas como exemplo ja que no video ele usa o nome do arquivo diretamente no open('items.csv', 'r')

        Pois da maneira abaixo posso instanciar diferentes tipos de Item a partir de csvs diferentes, voltar a pesquisar Decorators
        principalmente a partir dos exercicios ja feitos no arquivo decorators.py
        """
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            """
            Usa os items carregados como dicionarios em uma lista iterativa
            para instanciar os objetos da classe Item através dos valores das chaves
            """
            Item(
                Item(
                    name = item.get('name'),
                    price = float(item.get('name')),
                    quantity= int(item.get('name'))
                )
            )
    
    @staticmethod
    def check_nums(num) -> bool:    
        #Pesquisar mais sobre as diferenças e melhores casos para obter os melhores recursos entre STATIC e CLASS methods
        if isinstance(num, int):
            return True
        else: 
            return False