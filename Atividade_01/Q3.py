import requests
import requests_cache
from bs4 import BeautifulSoup
import re

def main():
  termo = input('Digite uma termo a ser buscado: ')

  regex(termo)


def create_cache():
  requests_cache.install_cache('buscadore de palavras e arredores')

def make_site_request():
  response = requests.get('https://www.bbc.com/portuguese')
  soup = BeautifulSoup(response.text, 'html.parser')
  texto = soup.get_text()
  return texto

def regex(termo):
  padrao = re.compile(r'(\b\w+\b.{0,20})?(' + re.escape(termo) + r')(.{0,20}\b\w+\b)?')
  ocorrencias = re.findall(padrao, make_site_request())

  print(ocorrencias)

if __name__ == "__main__":
  main()