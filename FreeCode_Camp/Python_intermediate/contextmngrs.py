#Alocar e liberar recursos sem chamar explicitamente basta colocar com with 

#Dessa maneira garante-se de abrir o arquivo, fazer o processo de escrita e demais operacoes, e ao final nao eh necessario fechar ou salvar o arquivo
with open('notes.txt', 'w') as file:
    file.write('Teste de escrita de arquivo com context manager')

#Sem context manager ficaria desse jeito, logo o jeito acima é mais "Limpo" para se trabalhar
file = open('notes2.txt', 'w')
try:
    file.write('Salvar arquivo com conteudo usando bloco tradicional de try finally')
finally:
    file.close()


#Pesquisar mais sobre isso, mas aparentemente pode-se criar classes para ser utilizado como context managers, bastando implementar os metodos __enter__ e __exit__
#Voltar nessa ultima classe mais pra frente, para mais exemplos e testes
class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exit')

