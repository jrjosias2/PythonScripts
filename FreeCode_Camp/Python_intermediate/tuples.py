#Trabalhar com tuplas é mais performatico do que com listas, exemplos da aula com sys.getsizeof, e o timeit, timeit mostrou mais eficência, tanto em CPU e armazenamento

#Similar as listas mas nao pode ter os objetos da lista alterados depois da criacao, e ao inves de [] usa-se (), ou sem nada
#As demais funcoes sao as mesmas das listas para iterar, acessar por slicing, mas nao pode-se atribuir ou remover itens
#E possivel converter listas para tuplas e vice-versa atraves da funcao de cast list(tupla) ou tuple(lista)

myTuple = ("Max", 30, "Temperatura", 16, "Umidade")
print(f"Stdout de tupla acima {myTuple}")
print(f"Stdout do tamanho de elementos na tupla {len(myTuple)}")
print(f"Stdout do index para Temperatura {myTuple.index('Temperatura')}")

#Slicing utilizando o step ultima casa para pular os elementos inicio:final:step
print(myTuple[2:5:2])
#Slicing dessa maneira, inverter a tupla
print(myTuple[::-1])

#Recurso interessante é que pode-se declarar variaveis de atribuicao para os elementos da tupla, ou tbm declarar *ponteiros, que vao funcionar como listas
v1, v2, v3, v4, v5 = myTuple

print(f"V1 {v1}")
print(f"V2 {v2}")
print(f"V3 {v3}")
print(f"V4 {v4}")
print(f"V5 {v5}")

# Quando não existem variaveis suficientes para fazer o unpacking / unboxing dos indices de uma Tupla,
# Colocar variaveis apenas para a quantidade correspondende aos indices iniciais 
# para os demais colocar uma variavel com * a frente que funciona como um ponteiro com a lista de valores remanescentes na tupla
p1, p2, *p3 = myTuple

print(f"P1 {p1}")
print(f"P2 {p2}")
print(f"P3* que vira lista {p3}")

p4, *p5 = myTuple

print(f"P4 {p4}")
print(f"P5 {p5}")

