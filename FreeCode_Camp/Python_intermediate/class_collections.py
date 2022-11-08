#Collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

#importa os elementos como chaves e valores de dicionarios, porém considerando o elemento como chave, e a qtd em que ele se repete o valor
a = "aaaaaaabbbbbbccccddddrrrrrrhhhhhggggggjjjjjjjnnnnnnnnnn"
mycounter = Counter(a)
print(mycounter.items())

#Retorna os itens que sao mais comuns dentro da colecao, o N dentro da funcao e a qtd de grupos
print("3 grupos mais comuns na collection: ", mycounter.most_common(3))

#Eh possivel navegar ainda mais para fazer slicing, pois a funcao retorna uma lista, podemos navegar para o conjunto ou para a chave
#primeiro com o conjunto
print("Conjunto de chave e valor do primeiro item: ", mycounter.most_common(3)[0])
#segundo com as chave
print("Mostrando somente a chave do primeiro item: ", mycounter.most_common(3)[0][0])
#terceiro com o valor
print("Mostrando o valor da chave: ", mycounter.most_common(3)[0][1])

#NAMED TUPLE, funciona como uma Struct, passa-se os atributos desejados, e depois basta iniciar como se fosse uma classe ou chamada de funcao
#Os valores informados podem ser acessados, diretamente como atributos da classe ou indices de lista
Point = namedtuple('Point', 'x,y')
pt = Point(10, 45)
print(pt)
print(pt[0], pt[1]) #ACESSO TIPO LISTA
print(pt.x, pt.y) #ACESSO VIA ATRIBUTO

#ORDEREDDICT, dicionarios em versoes antigas de python para lembrar as posicoes de insercao, nao serve pra muita coisa hoje NEM GASTAR ENERGIA

#DEFAULTDICT, dicionario padrao, porem caso o valor de uma chave nao seja atribuido explicitamente, ou se uma chave nao criada for acessada,
#  ao inves de retornar um erro, um valor padrao e atribuido.
d1 = defaultdict(float)
d2  =defaultdict(str)

d1['a'] = 10.30
d1['b'] = 10.45
d1['c'] = 10.70

d2['a'] = 'Josa'
d2['b'] = 'Futebol'
d2['c'] = 'Musculacao'

print(d1['f'])
print(d2['j'])

#DEQUE é como uma lista porem permite manipular melhor a inclusao e remocao de itens selecionando se a operacao vai acontecer no inicio ou final
# Pesquisar melhor depois as funcionalidades, mas basicamente as mesmas funcoes de lista, mas escolhe-se left/right appendleft(),
