#Pesquisar melhor como se trabalha com esses dicionarios com tuplas de multi index na chave
#Só funciona com tuplas, pesquisar melhor também por tbm

mytuple = (8,7)
mydict = {mytuple: 30, "10": 10}

print("Dict com Tupla de chave: ", mydict)

for key, value in mydict.items():
    print(key, ":", value)

print("somente as chaves")
for key in mydict:
    print(key)

#funciona em tese como um valor absoluto da chave, como se 8,7 fosse a chave por sí só e nao os 2 elementos como na tupla
key = mydict[8,7]

print("Valor do Key: ", key)