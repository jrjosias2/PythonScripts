#Parametros sao os atributos definidos na assinatura da funcao, enquanto Argumentos sao os valores atribuidos para esses atributos, 
# ex print_name(nome) -->> print_name('Josias') ... nome é o Parametro da funcao print_name, enquanto Josias e o argumento passado para a funcao


def global_Var_access():
    #gl_var_num = 10
    global gl_var_num
    gl_var_num = 3
    print('Insider: ', gl_var_num)

#Funcionou quando se coloca a keyword global seguido do nome da variavel, pois ai ele sabe que estamos falando da variavel de fora da funcao
gl_var_num = 0
#Chamando a funcao para acessar variavel global
global_Var_access()
print('Global: ', gl_var_num)

def foo(a, b, c):
    print(a, b, c)

#Parametros Padrao/Default, é quando na assinutura da funcao, o atributo ja tem um valor pre-definido, ou seja se especificado na chamada, ele eh substituido
def foo2(a, b, c, d=5):
    print(a, b, c, d)

# *args significa que qq numero de argumentos positional podem ser passados, se tiver com **kwargs pode ser passado com qq numero de keyword(chave/valor) argumentos
# args e kwargs sao so um padrao, podem ser chamados de qq coisa o que importa é o *nome ou **nome para determinar o comportamento, ** funciona como dicionarios key e values
def foo_args(a, b, *args, **kwargs):
    print(a, b)

    for arg in args:
        print(arg)

    for key in kwargs:
        print(key, kwargs[key])

#Quando se deseja forcar que os argumentos sejam passados explicitamente pelo nome do parametro, deve-se utilizar o *, no exemplo abaixo esta somente com o args, 
# porem poderia ser uma assinatura como foo_enforce(a, b, *, multiplicador, fator) aonde a e b, podem ser passados posicionalmente (somente os valores), 
# enquanto multiplicador e fator devem ser passados explicitamente -->> foo_enforce(1, 2, multiplicador=5, fator=3)
def foo_enforce(*args, last):
    for arg in args:
        print(arg)
    print(last)

#Unpacking de funcoes, quando se tem uma funcao e uma lista com a mesma qtd de parametros, da pra fazer o unpacking dos valores da lista/tupla, 
# unico ponto é colocar o *seguido do nome da lista, funciona tbm com dicionario, porem as chaves do dicionario devem seguir os mesmos da assinatura da funcao e deve-se usar **seguido do nome do dic
my_list = [5, 8 , 14]
my_dict = {'a': "TCS", 'b': "JnJ", 'c': 'LAS squad'}
foo(*my_list)
foo(**my_dict)

foo("Josias", "Leonardo", "JR")

#quando passar os argumentos explicitamente, deve-se fazer para todos os argumentos na sequancia do primeiro
foo2(c = "Josias", b = "Leonardo", a = "JR", d="TCS")
foo2("Josias", "Leonardo", "JR", )

#Aqui apos o segundo argumento, todos os demais até o 14 são posicionais, e os no formato chave/valor sao os kwargs
foo_args(10, 25, 8, 6, 9, 14, nome="josias", sobrenome="Leonardo Junior", CPF="322.348.038-29")

#Com excecao dos primeiros 2 argumentos que sao mandatorios, todos os demais, pode ser passado opcionalmente
foo_args(25, 1983, "Outubro", "Terça-feira")

foo_args(10, 9, nascido_em="25/10/1983", cidade_uf="Santos-SP")


#Operadores com *
resultado = 2*4
print("Usando somente * multiplicacao simples: ", resultado)

resultado = 2**4
print("Usando somente ** operador de potencial: ", resultado)

#Multiplica o tamanho da lista pelo conjunto de elementos
zeros = [0] * 10
print("Lista de 0s: ", zeros)

"Multiplica ABs por 10"
ABs = "AB" * 10
print("Lista de ABs: ", ABs)


#Fazer unpacking de lista, a variavel que tem o * vai ser o que vai herdar a lista, 
# considerando que ele atribui cada elemento da lista para cada variavel antes ou apos de declarar a varivavel a receber a lista
my_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

beginning, second, third, fourth, *middle, late_middle, start_last, last = my_numbers
print(beginning)
print(second)
print(third)
print(fourth)
print(middle)
print(late_middle)
print(start_last)
print(last)

my_tuples = (1,2,3)
my_numList = [4,5,6]

merged_list = [*my_tuples , *my_numList]

print("Tuplas: ", my_tuples, "\nLista: ", my_numList, "\nMerged Lista: ", merged_list)

#Copy, shallow e deep
#Mutable types, funciona ok, porque o python sempre cria uma nova copia, referencia, porem para valores imutaveis ou listas, deve se tomar cuidado, pois alterar a copia, tambem afeta o origem
#Para evitar isso tem a biblioteca copy import copy, voltar nessa aula depois, ou pesquisar mais sobre isso... mas basicamente DeepCopy mantem as referencias independentes
org = 5
cpy = org
cpy = 10
print(org, cpy)