#Importantissimo para manipular arquivos de chave-valor, principalmente json... precisamos dominar isso meu precioso
#Principais caracteristicas sao: Pares de chave e valor nome: valor_do_nome, Desordenada, Mutavel
myDict_1 = {"Nome": "Josias", "idade": 39, "dt_nascimento": "25/10/1983", "Natural": "Santos", "Estado": "SP"}
print(myDict_1)

#Outra forma mais simples de declarar o dictionary é atraves do cart dict(chave=valor,....)
myDict_2 = dict(Nome="Alexandre", idade=30, cidade="Sao Vicente")
print(myDict_2)

#novas chaves podem ser adicionadas simplesmente pela criacao dinamica do mesmo, por exemplo com o email
#no evento de um novo valor ser adicionado para a chave ja existente, o valor anterior eh substitituido
myDict_2["email"] = "jr.josias2@gmail.com"
print(myDict_2)

myDict_2["email"] = "jr.leo.josias2@gmail.com"
print(myDict_2)

#remover item pode ser o del dict[chave] ou pop("chave") ou tbm popitem() para remover o ultimo cj de chave-valor
del myDict_1["idade"]
print(myDict_1)

myDict_2.pop("cidade")
print(myDict_2)

myDict_1.popitem()
print(myDict_1)

#Usando a ultima chave Natural, tentei com estado apos a remocao e vai no else.
if 'Natural' in myDict_1:
    print("Estado de origem: ", myDict_1["Natural"] )
else:
    print("nao achou chave")

try:
    print("Bloco Try, except:", myDict_1["SobreNome"])
except:
    print("erro nao existe a chave")

#Iteracao em dicionarios, pode ser pelas chaves, valores ou amboes.
for key in myDict_1.keys():
    print(key)

for value in myDict_1.values():
    print(value)

for key, value in myDict_1.items():
    print(key, ":", value)

#O mesmo cuidado ao copiar com o operador = deve ser tomado aqui também, deve-ser as funcoes .copy ou dict(dictionary)

#Fazer o merge de dicionarios, basta usar a funcao update(dictionary a ser feito o merge), as chaves existentes nao sao atualizadas, as novas sao inseridas.
myDict_1.update(myDict_2)
print(myDict_1)

