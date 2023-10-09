import requests

from acesso_CEP import BuscaEndereco
cep = "03726040"
obj_cep = BuscaEndereco(cep)

#r = requests.get('https://viacep.com.br/ws/01001000/json/')
#print(r.text)

bairro, cidade, uf = obj_cep.acessa_CEP()
print(bairro, cidade, uf)


