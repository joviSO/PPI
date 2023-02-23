import requests
import requests_cache
from bs4 import BeautifulSoup

def main():
  create_cache()

  find_tag_a(BeautifulSoup(make_request().text, 'html.parser'))
  
def create_cache():
  requests_cache.install_cache('Tag A')

def make_request():
  return requests.get('https://www.reddit.com/r/investimentos/')

def find_tag_a(resposta):
  links = resposta.find_all('a')
  for link in links:
    texto = link.get_text("")
    linkado = link.get("href")
    print(texto, " - " ,linkado)

if __name__ == "__main__":
  main()
