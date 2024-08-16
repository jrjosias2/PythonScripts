#Sets sao criados como dicionarios, e também como dicionários não permitem valores duplicados.
#Existe tambem o frozenset que funciona de maneira imutavel, nao pode ser alterado apos a criacao
#Funcoes para atualizar, basta usar os metodos, add(), remove(), discard(), clear(), pop()

#Funcao union faz o merge de 2 sets ordenado e sem duplicar os valores
#Pesquisar demais funcoes como intersection() pega elementos em 2 sets,  difference() retorna os elementos do primeiro set que nao existem no segundo
#Symetric_difference, retorna os elementos diferentes em ambos os sets. 
#Essas funcoes nao modificam os sets originais, para fazer a alteracao tem de usar o update() 
#ou intersection_update() esse mantem somente os valores encontrados em ambos os sets
#difference_update() atualiza somente os valores não encontrados no segundo set
#symmetric_difference_update cria um set com os valores diferentes entre 2 sets, somente os valores distintos sao usados para criar o novo set
#issubset retorna TRUE ou FALSE, se um set tem todos os elementos do segundo entao retorna TRUE, e o issuperset() inverso, importante saber 
#se todos os elementos de um set existem no outro, para depois pegar a diferenca
#isdisjoint() so retorna TRUE, se o set comparado tem elementos nao existentes no primeiro
#https://docs.python.org/2/library/sets.html

myset = {1,2,3,5,7,9,1,3,4,11,10,1,2,8}

print(f"Stdout para validar remoção automática de registros duplicados {myset}")

myset.add(6)
myset.remove(11)
print(f"Stdout apos add o valor 6, e remover o valor 11 {myset}")

for x in myset:
    print(x)

if 10 in myset:
    print("yes")
elif 11 in myset:
    print("yes")
else:
    print("melou")
