class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia!")

    def get_url_base(self):
        ind_int = self.url.find('?')
        url_base = self.url[:ind_int]
        return url_base

    def get_url_param(self):
        ind_int = self.url.find('?')
        url_param = self.url[ind_int + 1]
        return url_param

    def get_valor_param(self, param_busca):
        ind_param = self.get_url_param().find(param_busca)
        ind_valor = ind_param + len(param_busca) + 1
        ind_e_com = self.get_url_param().find('&', ind_valor)
        if ind_e_com == -1:
            valor = self.get_url_param()[ind_valor:]
        else:
            valor = self.get_url_param()[ind_valor:ind_e_com]
        return valor


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
valor_quant = extrator_url.get_valor_param("quantidade")
print(valor_quant)
