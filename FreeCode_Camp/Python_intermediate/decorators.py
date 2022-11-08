#Decorators Funcoes e Classe, decorator eh uma funcao que pega uma outra funcao como argumento e estende o comportamento dessa funcao
#Exemplo abaixo das funcoes, para usar uma funcao com o decorator tem que colocar o @nome da funcao, nesse caso dentro da funcao decorator, se coloca toda a logica
# e a melhor maneira de estender a funcao sendo decorada

#na Pratica o que o decorator faz é atribuir para uma funcao, o comportamento da funcao decoradora, usando de argumento a funcao a ser decorada
# ficaria algo como print_name = start_end_decorator(print_name)

#PESQUISAR mais sobre Class Decorators que mantem o estado das variaveis, por exemplo armazenar o numero de vezes que uma funcao eh chamada, e tbm o aninhamento de decorators

import functools

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Something before extending")
        inner_result = func(*args, **kwargs)
        print("Func extended: ", func.__name__)
        print("something after extending")
        return inner_result
    return wrapper

#Decorator com argumentos, no exemplo é de repeticoes, a funcao repeat tem argumento numerico, e o decorator para receber a funcao como argumento (decorada), 
# e o wrapper para executar a estensão da funcao decorada
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func_result = func(*args, **kwargs)
            return func_result
        return wrapper
    return decorator_repeat

@start_end_decorator
def print_name(nome):
    print(nome)

def print_name_age(nome, idade):
    print("Nome: ", nome, "\nIdade: ", idade)

@start_end_decorator
def sum5(x):
    return x+5

#Decorator Boas Praticas
print_name("Josa")

#Decorator raiz hard_coded
print_name_age = start_end_decorator(print_name_age)
print_name_age("Josias", 39)

#Essa funcao tem como retorno None, porque o resultado da operacao que eh usada no wrapper do decorator nao tem nenhum retorno,
# entao deve-se inserir la uma variavel para recebecer o valor de func(*args, **kwargs), e ao final de tudo fazer o return, apos atualizar isso, o resultado da soma e mostrado
print("Resultado da Funcao sum5:\n", sum5(10))

#usando o functools, e estendendo o proprio como decorator do wrapper da nossa funcao decorator, ele preserva a identidade do caller 
# pois quando se usa as funcoes help ou imprimir o nome da funcao no evento de error handling, o nome ira aparecer como sendo wrapper
#BOA PRATICA EM PYTHON, PESQUISAR MAIS SOBRE ESSA CLASSE E COMO USAR DECORATORS, UTIL PRA CARALHO.
print("Help da Funcao: ", help(print_name))
print("Nome da funcao", print_name.__name__)

@repeat(num_times=3)
def salve(name):
    print(f'Fala fiii du Bill {name}')

salve("Mauricio")