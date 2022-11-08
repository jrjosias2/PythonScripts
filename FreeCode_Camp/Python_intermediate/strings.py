from timeit import default_timer as timer

#Tem outras funcoes basicas alem do split, como o strip para remover espacos em branco a esquerda e direita,  start/endsWith e outros... nao sao tao cricas
# pesquisar mais de acordo com cada necessidade

my_string = 'how,are,you,doing,buddy'
my_list = my_string.split(",")
print(my_list)

#Sempre dar preferencia para utilizar a funcao join de string por ser mais performatica e utilizar muito menos recursos do que as funcoes padroes de atribuicao com +=
new_string = ' '.join(my_list)
print(new_string)

chain_string = ['A'] * 6000000
new_chain = ''

#BAD CODE
start = timer()
for i in chain_string:
    new_chain += i
stop = timer()
print("Bad code time cost: ", stop-start)

#IDEAL CODE
start = timer()
new_chain = "".join(chain_string)
stop = timer()
print("Ideal code time cost: ", stop-start)

#Pesquisar f-Strings para formatacao de strings, mas basicamente se coloca o f antes da string e dentro dela as {var}, {var}, {n}
var1 = 10
var2 = 14.2578
my_str_test = f"Os valores de variaveis dinamicos sao {var1} e tambem {var2: .2f}, podendo tambem usar campos diretamente como agora {'Josias'.upper()} {'LEONARDO'.lower()}"
print(my_str_test)


