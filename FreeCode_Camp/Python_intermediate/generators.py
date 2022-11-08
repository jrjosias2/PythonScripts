#Generators sao funcoes que retornam funcoes iteraveis, eficientes em memoria e util para trabalhar com grandes datasets
#PESQUISAR MELHOR, PARECE UTIL, PRINCIPALMENTE PARA TRABALHAR COM LISTAS DE NUMEROS

def mygenerator():
    yield 1
    yield 5
    yield 25

def mygenerator_string():
    yield "Josias"
    yield "Leonardo"
    yield "Junior"

#FUNCIONA O GENERATOR COM LISTAS E DICIONARIO, NESSE CASO ENTAO PESQUISAR MAIS AS FUNCOES PARA PERCORRER PRINCIPALMENTE DICIONARIOS E AVALIAR A PERFORMANCE.
def mygenerator_dict():
    yield {"nome": "Josias", "idade": "39", "Profissao": "Arquiteto de Dados", "Empregador": "TCS"}
    #yield dict(nome = "Josias", idade="39", Profissao="Arquiteto de Dados", Empregador="TCS") funciona dos 2 jeitos de atribuicao
    yield ['Josias', 'Leonardo', 'Junior']

g = mygenerator()
gs = mygenerator_string()
gdct = mygenerator_dict()

#for i in g:
#    print("Iterator in: ", i) 

#Funcao para pegar o prox valor da lista, a vantagem eh que durante a execucao, toda vez que chamar Next, ele salva o ponto de partida anterior
value = next(g)
print("Next: ", value)

value = next(g)
print("Next: ", value)

value_str = next(gs)
print("Next: ", value_str)

value = next(g)
print("Next: ", value)

value_str = next(gs)
print("Next: ", value_str)

value_str = next(gs)
print("Next: ", value_str)

value_dict = next(gdct)
print("Next: ", value_dict)
value_dict = next(gdct)
print("Next: ", value_dict)


#ESSA ESTRUTURA NAO EH UMA BOA PRATICA, POIS VAI PRECISAR ARMAZENAR MAIS MEMORIA COM A LISTA
def firstn(n):
    nums = []
    num = 0
    while num < n:
        #print("valor de num Funcao Lista: ", num)
        nums.append(num)
        num += 1
    return nums

#ESSA E A MELHOR PRATICA USANDO GENERATOR POIS NAO PRECISA DA LISTA E O RESULTADO EH O MESMO
def firstn_generator(n):
    num = 0
    while num < n:
        #print("valor de num Generator: ", num)
        yield num
        num += 1

def regular_sum(n):
    num = 0
    while num < n:
        num += 1
    return num

import sys

print("Sum firstn: ", sum(firstn(5)))
print("Sum firstn_gen: ",sum(firstn_generator(5)))

#Interessante que para a funcao sizeof do Generator, ele não precisou entrar dentro da funcao, pois ja tem os valores em memoria, entrou na regular, 
# e o size acabou por sendo menor, mas creio que para funcoes complexas que necessite percorrer listas, tuplas etc, utilizar o Generator é realmente a melhor opcao

print("Size com lista: ", sys.getsizeof(firstn(1000000)))
print("Size com generator: ", sys.getsizeof(firstn_generator(1000000)))
print("Size com funcao regular: ", sys.getsizeof(regular_sum(1000000)))

#Funciona da mesma maneira como acessar o kwargs, ver se é possivel navegar dentro dos elementos, pois assim vai ser possivel designar para um dicionario.
def generator_dict_list(gen_dict):
    for key in gen_dict:
        print(key)

gdct = mygenerator_dict()
generator_dict_list(gdct)