
## 5) Observando e salvando as informações coletadas

data_team.head(10)

data_team.info()

data_team = data_team[['Id_team','Name_team', 'Url_team', 'Id_league', 'Name_league', 'Country_league', 'Url_league', 'Overall', 'Attack', 'Midfield', 'Defence', 'Tranfer Budget']]

data_team.to_csv('df_team.txt',sep=';',index=False, encoding='utf-8')