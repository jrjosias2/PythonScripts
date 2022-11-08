#Pelo o que entendi o mais importante aqui é usar o multi-threading ja que a gestão de processo e mais trabalhosa e arriscada por questões de implementacao do python
#Pesquisar mais, pois para criar multi-threading para manipular grandes datasets ou demais conexoes podem ser interessantes

from multiprocessing import Process
from threading import Thread
import os, time

def square_number():
    for i in range(5):
        print(i)
        #i * i
        print(i)
        time.sleep(0.2)

threads = []
num_threads = os.cpu_count()

print("nro de threads baseado na qtd de CPU do PC", num_threads)

#process creation
for i in range(num_threads):
    p = Thread(target=square_number)
    threads.append(p)
    print(threads.__str__())

#start
for p in threads:
    p.start()

#join espera a conclusao da thread anterior para iniciar a nova
for p in threads:
    p.join()

print('final da Main')




