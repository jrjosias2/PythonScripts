from item import Item

class Mobile_phone(Item):

    def __init__(self, name: str, price: float, quantity: int = 0, brand: str = '', newly_phone: bool =True) -> None:        
       super().__init__(name, price, quantity)
       self.brand = brand
       self.newly_phone = newly_phone

    '''
        ABSTRACAO
        É a capacidade da classe ter privado a ela alguns metodos e demais recursos que são de responsabilidade dela acessar e modificar
        nesse exemplo para um envio de email, vamos deixar publico somente o send email, enquanto quaisquer demais operacoes, devem ficar a cargo
        de metodos privados a class, que serao acessados diretamente de dentro do metodo send_email
        Para converter um metodo para Privado, usa-se o __ da mesma maneira que para atributos de classe

        Os 3 metodos de acesso interno, não são visiveis no arquivo oop.py na instancia phone1
    '''

    def __connect_smtp(self, smtp_server):
        pass

    def __prepare_email_body(self):
        return 'Teste'

    def __verify_attachment(self, file):
        pass
    
    def send_email(self):
        self.__connect_smtp('Teste')
        self.__prepare_email_body()
        self.__verify_attachment('file')
        pass