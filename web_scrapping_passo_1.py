from requests import get

url = 'https://sofifa.com/teams?offset=0'

response = get(url) 

from bs4 import BeautifulSoup

soup_teams = BeautifulSoup(response.text, 'html.parser')

# Bloco de informações gerais dos Times
soup_teams.findAll('td', class_ = 'col-name-wide')