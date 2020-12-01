## 2 ) Acessando as informações do 1 time Registrado

# Primeiro : Bloco de informações gerais dos Times
soup_teams.find('td', class_ = 'col-name-wide')

# ID do Time 
soup_teams.find('td', class_ = 'col-name-wide').a.get('href').split('/')[2]

# Site do Time 
soup_teams.find('td', class_ = 'col-name-wide').a.get('href')

# Nome do Time
soup_teams.find('td', class_ = 'col-name-wide').div.get_text()

# ID da Liga que está incluido
soup_teams.find('td', class_ = 'col-name-wide').findAll('a')[1].get('href').split('=')[1]

# Site da Liga 
soup_teams.find('td', class_ = 'col-name-wide').findAll('a')[1].get('href')

# Nome da Liga que está incluido
soup_teams.find('td', class_ = 'col-name-wide').findAll('a')[1].get_text()	

# Pais que o Time Joga
soup_teams.find('td', class_ = 'col-name-wide').findAll('a')[1].div.img.get('title')

# Indicador  Geral de performance do time
'Overall'
soup_teams.find('td', class_ = 'col col-oa').get_text()

'Attack'
soup_teams.find('td', class_ = 'col col-at').get_text()

'Midfield'
soup_teams.find('td', class_ = 'col col-md').get_text()

'Defence'
soup_teams.find('td', class_ = 'col col-df').get_text()

'Tranfer Budget'
soup_teams.find('td', class_ = 'col col-tb').get_text()
