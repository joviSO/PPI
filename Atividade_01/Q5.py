import requests
import requests_cache
from bs4 import BeautifulSoup

def main():

  create_cache()

  response = BeautifulSoup(
              requests.get(
                  "http://www.google.com/search?q=" + input("busca: ").replace(" ", "+")
              ).text, 'html.parser'
             )

  print(response)

def create_cache():
  requests_cache.install_cache('Script Google')

if __name__ == "__main__":
    main()