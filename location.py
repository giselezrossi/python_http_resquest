#pip install requests

import requests

URL = "https://randomuser.me/api/0.7"


result = requests.get(url=URL)

data = result.json()

name = data['results'][0]['user']['name']['first']
last_name = data['results'][0]['user']['name']['last']
user_name = data['results'][0]['user']['username']
phone = data['results'][0]['user']['phone']

print('nome: ' + name)
print('sobrenome: ' + last_name)
print('usuário: ' + user_name)
print('telefone: ' + phone)