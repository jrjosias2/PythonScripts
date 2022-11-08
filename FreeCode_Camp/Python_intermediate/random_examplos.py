#Pode ser relevante pra algumas funcoes, principalmente o randon.normalvariate, choice e sample, choices (similar choice, mas escolhe elementos repetidos)
#PEsquisar o que o random.seed pode ser aplicado e tambem o secrets

import random

a = random.random()
b = random.uniform(1, 10)
c = random.randint(1, 10)
d = random.normalvariate(0, 1)
print(a, b, c, d)
