'''
Python: 2
Programa: Crawler
'''

# Bibliotecas
import sys
import bs4
import time
import requests

while True:

    try:
        # Configuracoes
        url = "https://g1.globo.com"
        cabecalho = {"user-agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)"}

        # Html aperfeicoado
        html = requests.get(url=url, headers=cabecalho).text
        html_super = bs4.BeautifulSoup(html, "html.parser")

        # Crawler
        noticias = html_super.find_all(class_="feed-post-link gui-color-primary gui-color-hover")
        imagem = html_super.select("picture > img")
        #imagem = html_super.find_all("img", attrs={"class": "bstn-fd-picture-image"})

        print("\n *** Principais noticias *** ")
        for i in range(0, len(noticias)):

            print("\n * Noticia [" + str(i+1) + "] : " + noticias[i].get_text())
            print(" - Link: " + noticias[i].get("href"))


        print("\n *** Principais imagens *** ")
        for j in range(0, len(imagem)):

            print("\n - Titulo: " + str(imagem[j].get("title")))
            print(" * Link: " + imagem[j].get("src"))

        print("\n\n - Dentro de 10 segundos site atualizara...")
        time.sleep(10)

    except Exception as e:
        print(e)
        pass
