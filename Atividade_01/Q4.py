import requests
import requests_cache
def main(): 
  create_cache()

  create_image()

def create_image():
  with open('imagem_legal.jpg', 'wb') as imagem:
    resposta = requests.get("https://pbs.twimg.com/media/FpM0YeiXoAE0sYa?format=jpg&name=large", stream=True)
    
    #aqui foi tirado diretamente de algum codigo do Stackoverflow, não sabia como buildar a imagem
    if not resposta.ok:
      print("Ocorreu um erro, status:" , resposta.status_code)
    else:
      for dado in resposta.iter_content(1024):
        if not dado:
            break

        imagem.write(dado)

def create_cache():
  requests_cache.install_cache('Download de Imagem')

if __name__ == "__main__":
  main()