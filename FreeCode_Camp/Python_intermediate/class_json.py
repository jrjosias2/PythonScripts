#Parece simples demais pra ser verdade, pesquisar mais esse exemplo e as principais funcoes
import json

person = dict(nome="Josias", idade=39, cidade="Sao Paulo", TemFilhos=False, Titulos=["Engenheiro de Dados", "GCP", "AWS", "Python", "Arquiteto de Solucoes"])
print('Person Items:\n', person.items())

#Python dict to Json
personJSON = json.dumps(person, indent=4)
print('Person parsed by json.dumps:\n', personJSON)

pos = person['Titulos'].index('Python')
person['Titulos'].remove('GCP')
person['Titulos'].append('GCP K8S')
person['Titulos'].append('GCP Data Engineer')
print(person.items())

#Save it in json format
with open('person_dict.json', 'w') as file:
    json.dump(person, file, indent=4)

with open('person_str.json', 'w') as file:
    json.dump(personJSON, file, indent=4)

#Qdo carregado na memoria ou através de Arquivo Texto se usa sempre o loads ou dumps aonde o s significa string ou direto do stream, enquanto sem o s significa salvar, ler o arquivo fisico em disco
person2 = json.loads(personJSON)
print('Loads from personJson:\n', person2)

with open('person_dict.json', 'r') as file:
    person3 = json.load(file)
    print('File loaded:\n', person3)

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
user2 = {'name':'Josias', 'age' : '40'}

userJSON = json.dumps(user, default=encode_user)
print('Parsed by json.dumps:\n', userJSON)

# Como nao e uma instancia da classe User, ele nao entra no metodo encode_user da classe acima
userJSON2 = json.dumps(user2, default=encode_user)
print('Parsed by json.dumps:\n', userJSON2)

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

userJSON = UserEncoder().encode(user)
print("User Encoder", userJSON)

userDict1 = UserDecoder().decode(userJSON)
print("User decoder", userDict1)

#Aqui ele tbm nem entra no UserEncoder, porque nao ha necessidade de fazer o Encode do user2, ja que o mesmo é um dict/json format type
userJSON2 = UserEncoder().encode(user2)
print("User Encoder 2", userJSON)

userDict1 = UserDecoder().decode(userJSON2)
print("User decoder 2 ", userDict1)