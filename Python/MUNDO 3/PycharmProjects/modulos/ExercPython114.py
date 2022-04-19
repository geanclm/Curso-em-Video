# Exercício Python 114: Crie um código em Python que teste
# se o site pudim está acessível pelo computador usado.
# ---
# by geanclm in 19/04/2022 at 17:30h
# ---
import urllib.error
from bs4 import BeautifulSoup
import requests
url = 'http://www.pudim.com.br/'

try:
    response = requests.get(url)
except urllib.error.URLError:
    print(f'O site {url} está Offline. Favor verificar a disponibilidade do serviço!')
else:
    print()
    print (f'o site {url} está Online')
    print()
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup.prettify())
