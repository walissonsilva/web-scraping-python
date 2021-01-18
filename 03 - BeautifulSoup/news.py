import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML da notícia
noticia = site.find('div', attrs={'class': 'feed-post-body'})

# Título
titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

print(titulo.text)

# Subtítulo: div class="feed-post-body-resumo"
subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

print(subtitulo.text)