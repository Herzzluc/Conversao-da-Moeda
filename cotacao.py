import urllib.request as req
import re

real = float(input('Informe o valor desejado '))


class Cotacao:

    def __get_cotacao(self, url, regex='^.*nacional" value="([0-9,]+)"'):
        pagina = req.urlopen(url)
        s = pagina.read().decode('utf-8')

        m = re.match(regex, s, re.DOTALL)
        if m:
            return float(m.group(1).replace(',', '.'))
        else:
            return 0

    def dolar(self):
        return self.__get_cotacao('http://dolarhoje.com/')

    def euro(self):
        return self.__get_cotacao('http://eurohoje.com/')

    def peso_argentino(self):
        return self.__get_cotacao('https://dolarhoje.com/peso-argentino/')


cotacao = Cotacao()


print('Hoje estamos com as seguintes contações de moedas estrangeiras')
print('Dolar: U$ {}'.format(real/cotacao.dolar()))
print('Euro: E$ {}'.format(real / cotacao.euro()))
print('Peso Argentino: ARS$ {}'.format(real/cotacao.peso_argentino()))

input('Pressione uma tecla para sair...')
