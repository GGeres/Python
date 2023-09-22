url = "bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"


ind_int = url.find('?')

url_base = url[:ind_int]


url_param = url[ind_int+1:]
print(url_param)

param_busca = 'quantidade'
ind_param = url_param.find(param_busca)
ind_valor = ind_param + len(param_busca) + 1

ind_e_com = url_param.find('&', ind_valor)
if ind_e_com == -1:
    valor = url_param[ind_valor:]
else:
    valor = url_param[ind_valor:ind_e_com]

print(valor)