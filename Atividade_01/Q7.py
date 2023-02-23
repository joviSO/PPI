import requests
import requests_cache

def main():
  url = 'https://viacep.com.br/ws/{}/json/'.format(input('Insira o cep: '))

  response = requests.get(url)
  print(response.text)

def create_cache():
  requests_cache.install_cache('Buscador de CEP')

if __name__ == "__main__":
  main()