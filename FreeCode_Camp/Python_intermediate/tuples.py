#Trabalhar com tuplas é mais performatico do que com listas, exemplos da aula com sys.getsizeof, e o timeit, timeit mostrou mais eficência, tanto em CPU e armazenamento

#Similar as listas mas nao pode ter os objetos da lista alterados depois da criacao, e ao inves de [] usa-se (), ou sem nada
#As demais funcoes sao as mesmas das listas para iterar, acessar por slicing, mas nao pode-se atribuir ou remover itens
#E possivel converter listas para tuplas e vice-versa atraves da funcao de cast list(tupla) ou tuple(lista)

myTuple = ("Max", 30, "Temperatura", 16, "Umidade")
print(myTuple)
print(len(myTuple))
print(myTuple.index("Temperatura"))
#Slicing utilizando o step ultima casa para pular os elementos inicio:final:step
print(myTuple[2:5:2])
#Slicing dessa maneira, inverter a tupla
print(myTuple[::-1])

#Recurso interessante é que pode-se declarar variaveis de atribuicao para os elementos da tupla, ou tbm declarar *ponteiros, que vao funcionar como listas
v1, v2, v3, v4, v5 = myTuple

print("\n", v1)
print(v2)
print(v3)
print(v4)
print(v5, "\n")

p1, p2, *p3 = myTuple

print(p1)
print(p2)
print(p3)

