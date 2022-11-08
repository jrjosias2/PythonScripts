#lambda argument: expression, tem a mesma funcionalidade de um metodo, porem eh criada em 1 linha, e pode ser usada como argumento de funcoes (key), 
# e mais util quando utilizado eh necessario utilizar somente 1x durante a execucao, no caso de precisar utilizar outras vezes com mais argumentos, pode-se criar as funcoes e chama-las
# vai ter o mesmo efeito. PROCURAR AS PRINCIPAIS DIFERENCAS E VANTAGENS PARA USAR LAMBDAS

from functools import reduce

add10 = lambda x: x+10
print(add10(3))

mult_lambda = lambda x,y: x*y
print(mult_lambda(5,6))

#Usando lambdas em funcoes in-built SORTED
points2D = [(1, 2), (5, 6), (4, 8), (-1, 10)]
points2D_sorted = sorted(points2D)
points2D_sorted_index = sorted(points2D, key=lambda x: x[1])
points2D_sorted_sum = sorted(points2D, key=lambda x: x[0] + x[1])

#Funcao abaixo exatamente a mesma funcionalidade que o codigo lambda utilizado para o sorted_index
def sort_by_y(x):
    return x[1]

print("Lista padrao: ", points2D)
print("Sorted padrao: ", points2D_sorted) #Ordena a partir do indice x da lista [-1, 1, 4, 5]
print("Sorted index: ", points2D_sorted_index) #Ordena a partir do incide y da lista [2, 6, 8, 10]
print("Sorted sum: ", points2D_sorted_sum) #Ordena a partir da soma do conjunto da lista [3, 9, 11, 12]

#Map transform cada elemento com uma funcao map(func, sequence)
l1 = [1, 2, 3, 4, 5]
l2 = map(lambda x: x*2, l1)
print("Map function: ", list(l2))

#List comprehension --> Se lê valor do elemento multiplicado por 2 para cada valor de elemento dentro da lista l1
l3 = [x*2 for x in l1]
print("List comprehension: ", l3)

#Filter retorna True ou False filter(func, seq)
f1 = filter(lambda x: x%2==0, l1)
print("Filtros para numeros pares: ", list(f1))

#Se lê --> Se o valor do elemento multiplicado por 2 sobrar 0, entao para cada elemento atribua a x
f2 = [x for x in l1 if x%2==0]
print("Filter com list comprehension: ", f2)

#Reduce pesquisar mais o que cada uma dessas funcoes fazem, principalmente Map, Filter e Reduce
#Repetidamente aplica uma funcao aos elementos da lista, e retorna somente 1 valor
reduceList_1 = [1, 2, 3, 4, 5, 6]

product_A = reduce(lambda x,y: x*y, reduceList_1)
print("Reduce func: ", product_A)
