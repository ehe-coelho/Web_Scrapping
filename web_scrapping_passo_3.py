## 3 ) Acessando informações de todos os Times da primeira página

from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


url = 'https://sofifa.com/teams?offset=0'
response = get(url) # urlopen( req )
soup_teams = BeautifulSoup(response.text, 'html.parser')

# Lista para salvar cada linha de informação
list_team = []

cont = 0
for card_team in soup_teams.findAll('tr'):
    
    if (cont % 10) == 0 :
        print('\n')
        print(cont)
        
    if cont > 1:
        
        # Discionário para pegar informações
        discionario_team = {}

        ref_team = card_team.find('td', class_ = 'col-name-wide')

        # ID do Time 
        discionario_team['Id_team'] = ref_team.a.get('href').split('/')[2]
        
        # Nome do Time
        discionario_team['Name_team'] = ref_team.div.get_text()

        # Site do Time 
        discionario_team['Url_team'] = ref_team.a.get('href')

        # ID da Liga que está incluido
        discionario_team['Id_league'] = ref_team.findAll('a')[1].get('href').split('=')[1]

        # Nome da Liga que está incluido
        discionario_team['Name_league'] = ref_team.findAll('a')[1].get_text()

        # Site da Liga 
        discionario_team['Url_league'] = ref_team.findAll('a')[1].get('href')
        
        # Pais que o Time está inserido
        discionario_team['Country_league'] = ref_team.findAll('a')[1].div.img.get('title')

        # Indicador  Geral de performance do time
        discionario_team['Overall'] = card_team.find('td', class_ = 'col col-oa').get_text()

        discionario_team['Attack'] = card_team.find('td', class_ = 'col col-at').get_text()

        discionario_team['Midfield'] = card_team.find('td', class_ = 'col col-md').get_text()

        discionario_team['Defence'] = card_team.find('td', class_ = 'col col-df').get_text()

        discionario_team['Tranfer Budget'] = card_team.find('td', class_ = 'col col-tb').get_text()
        
        
        # Adicionando resultado a lista
        list_team.append(discionario_team)
        
    # Contatodor
    cont += 1

# Criando um Dataframe com os resultados
data_team = pd.DataFrame(list_team)
data_team    