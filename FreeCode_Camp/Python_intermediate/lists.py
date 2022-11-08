
mylist = ["banana", "cereja", "maca", "morango"]
print("Lista de frutas", mylist)
print("Qtd de frutas na lista eh de:\n", len(mylist))

for i in mylist:
    print(i)

#Adicionar itens pode ser com o append, que adiciona ao final, ou o insert aonde deve-se passar a posiçao de insercao
mylist.insert(0, "limao")
mylist.append("abacaxi")
print(mylist)

#Remover pode ser com o pop() que remove o ultimo elemento, retornando ele para uma variavel, ou o remove("object"), ou limpar tudo com o clear()

itemRemovido = mylist.pop()
print("Item Removido da lista: \n", itemRemovido)
mylist.remove("banana")
print(mylist)
mylist.append(itemRemovido)
print("Adicionado novamente na lista: \n", mylist)

#ordernar a lista com reverse() ou entao ordenar com o sort(), tbm tem o sorted e reversed que tem a mesma funcao mais retornam uma nova lista.

mylist.reverse()
print("Lista reversa: ", mylist)
mylist.sort()
print("Lista ordenada: ", mylist)

#Slicing 
myNumberList = [1,2,3,4,5,6,7,8,9,10,11,12]
a = myNumberList[1:5]
print(a)

#Atribuicao de lista com o operador = deixa as listas referenciadas na memoria, sendo assim qualquer alteracao na lista original, vai impactar na copia
#para evitar isso deve-se usar a funcao .copy(), ou a funcao list(lista_orignal) ou o slicing como lista(:) que significa do inicio ao final, que vai criar uma nova lista em outro espaco de memoria
#Usei as 3 funcoes e realmente funciona bem

nameList = ["josias", "leonardo", "junior"]
cpnameList = nameList[:]
print("antes de atualizar somente a original\n",nameList, "\n", cpnameList)
nameList.append("Jose")
print("Apos atualizar somente a original\n", nameList, "\n", cpnameList)


