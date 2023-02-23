import requests
import requests_cache
from bs4 import BeautifulSoup

def main():
  create_cache()

  response_to_request(make_bbc_request(input("insira o valor nome de uma tag aqui: ")))

def create_cache():
  requests_cache.install_cache('Tags Gerais')

def make_bbc_request(tag):
  return BeautifulSoup(requests.get('https://www.bbc.com/portuguese').text, 'html.parser').find_all(tag)

def response_to_request(links):
  if links == []:
    print("A tag escolhida não retornou nada")
  else:
    for link in links:
      texto = link.get_text("")
      print(" - ", texto)

if __name__ == "__main__":
  main()
