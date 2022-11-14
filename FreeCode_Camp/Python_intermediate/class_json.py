#Parece simples demais pra ser verdade, pesquisar mais esse exemplo e as principais funcoes
import json

person = dict(nome="Josias", idade=39, cidade="Sao Paulo", TemFilhos=False, Titulos=["Engenheiro de Dados", "GCP", "AWS", "Python", "Arquiteto de Solucoes"])
print(person.items())

#Python dict to Json
personJSON = json.dumps(person, indent=4)
print(personJSON)

#Save it in json format
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)

#Qdo carregado na memoria se usa sempre o loads ou dumps aonde o s significa string ou direto do stream, enquanto sem o s significa salvar, ler o arquivo fisico em disco
person2 = json.loads(personJSON)
print(person2)

with open('person.json', 'r') as file:
    person3 = json.load(file)
    print(person3)

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

def encode_user(obj):
    if isinstance(obj, User):
        return {'name': obj.name, 'age': obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError('Objeto tipo User nao eh serializavel em JSON')

user = User('Josa', 40)

userJSON = json.dumps(user, default=encode_user)
print(userJSON)

#BEM MAIS FACIL
from json import JSONEncoder, JSONDecoder

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

class UserDecoder(JSONDecoder):
    def default(self, o):
        if User.__name__ in o:
            return User(name=o['name'], age=o['age'])
        return o

userJSON2 = UserEncoder().encode(user)
print(userJSON2)

userDict1 = UserDecoder().decode(userJSON2)
print(userDict1)