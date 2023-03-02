import requests
import requests_cache
from bs4 import BeautifulSoup
import re

def main():
  create_cache()

  termo_busca = "ruby"
  url = "https://www.ruby-lang.org/pt/documentation/"
  depth = 2

  print(busca(termo_busca, url, depth))

def create_cache():
  requests_cache.install_cache('Buscador')
  
def request_url(url):
  return requests.get(url)

def busca(termo, url_inicial, profundidade):
  
  urls = [url_inicial]

  visitados = []
  ocorrencias = {}
  for i in range(profundidade):
    novas_urls = []
    for url in urls:

      if url not in visitados:
        visitados.append(url)
        try:
          response = request_url(url)
        except:
          continue

        soup = BeautifulSoup(response.content, 'html.parser')
        padrao = re.compile(r'(\b\w+\b.{0,20})?(' + re.escape(termo) + r')(.{0,20}\b\w+\b)?')
        ocorrencias[url] = re.findall(padrao, soup.get_text())
        links = soup.find_all('a')

        for link in links:

          nova_url = link.get('href')
          novas_urls.append(nova_url)

    urls = novas_urls
    

  return ocorrencias
  
  
  
if __name__ == "__main__":
  main()


  