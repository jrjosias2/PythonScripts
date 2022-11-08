#TOOLS para manusear iterators for, while loops

from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat
import operator

#Product Funcao animal para fazer produto cartesiano diretamente em Python com listas, PESQUISAR MAIS, pode ser muito muito util mesmo com Data Science e Engineering
a = [1, 2]
b = [3, 4]
#Ainda é possível especificar a qtd de repeticoes possíveis, ex: product(a, b, repeat=2), isso pode ser muito valido tbm para estatistica
prod_cartesiano = product(a,b) 
print("Product: ", list(prod_cartesiano))

#Permutations cria todas as possíveis ordenacoes de um conjunto, legal tbm e ver como melhor aproveitar no dia a dia
p1 = [1,5,6]
permut = permutations(p1)
#Ainda é possível limitar a qtd de permutacoes por exemplo limitar a 2 conjuntos.
permut2 = permutations(p1, 2)
print("Permutation: ", list(permut))
print("Permutation c/ limite 2: ", list(permut2))

#Combinations combina todas as possiveis combinacoes com um tamanho especificado
#PEsquisar mais depois como melhor se aplica, pois a diferenca para o permutation com limite, eh que ele nao faz o shuffle dos demais numeros do conjunto
#so faz a combinacao do primeiro com o segundo e terceiro elemento, e do segundo com o terceiro
comb = combinations(p1, 2)
print("Combination: ", list(comb))

#Accumulate faz um iterator que retorna somas acumuladas, no exemplo acima 1, 6 e 12, sendo respectivamente 1, 1+5, 6+6
#Para usar outras funcoes deve-se importar a biblioteca operator para operacoes matematicas, e usa-la como segundo argumento da funcao, ou usar funcoes ja padrao como Max, Min etc
acc = accumulate(p1)
print(p1)
print("Std Sum: ", list(acc))

#Aqui usando o operator de multiplicacao, resultando em 1,5,30 | 1x1=1, 1x5=5, 5x6=30
acc2 = accumulate(p1, func=operator.mul)
print(p1)
print("Mul operator: ", list(acc2))

#GroupBy iterador que retorna chaves e grupos de um iteravel, sensacional funcao, pois da a oportunidade de agrupar os resultados
#dentro de uma funcao pre-estabelecida, no exemplo agrupa como False 3, 4 e True como 1, 2, e no exemplo por idade, agrupou os dicionarios por pessoas que tem a mesma idade

people = [
    {'nome': 'Tim', 'idade': 25}, 
    {'nome': 'Dan', 'idade': 25},
    {'nome': 'Claire', 'idade': 27},
    {'nome': 'Lisa', 'idade': 28},
]

g1 = [1,2,3,4]
gp_obj = groupby(g1, key=lambda x: x<3)

gp_obj2 = groupby(people, key=lambda x: x['idade'])

for key, value in gp_obj:
    print("Valores gp_obj: ", key, list(value))

for key, value in gp_obj2:
    print("Valores gp_obj2: ", key, list(value))

#Infinite Iterators as bibliotecas Count, Cycle e Repeat
#Count faz um loop infinito a partir de um número, e continua até que uma condicao quebre o loop.
for i in count(100):
    print(i)

    if i==110:
        break

#Cycle funciona como um loop infinito dentro de um ciclo (lista) ou iterable
cycle_1 = [1,2,3,4,5]
x = 0
#Coloquei aqui o X para criar um indice para condicionar a parada do loop
for i in cycle(cycle_1):
    print("index: ", x, "valor: ", i)
    x += 1
    if x==10:
        break

#Repeat funciona como o cycle, porém da pra colocar a qtd de repeticoes, e o retorno é uma lista
for i in repeat(cycle_1, 2):
    print("Repeat: ", i)
