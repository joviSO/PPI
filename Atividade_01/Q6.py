import requests
import requests_cache
from bs4 import BeautifulSoup


def main():
  link = 'https://www.meutimao.com.br/tabela-de-classificacao/campeonato_brasileiro/'

  print(create_table(link))

def create_cache():
  requests_cache.install_cache('tabela do brasileirão')

def make_request(link):
  response = requests.get(link)
  response_beaut = BeautifulSoup(response.text, 'html.parser')
  return response_beaut

def create_table(link):
  itens = make_request(link).find('table', attrs={'class':"classificacao_campeonato campeonato_brasileiro"})
  tabela = itens.text.strip()
  return tabela

if __name__ == "__main__":
  main()