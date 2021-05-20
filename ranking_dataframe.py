import pandas as pd
import csv,json
data=pd.read_excel('game_user_sample.xlsx',index_col=None)
data['diff']=data['games_played']-data['games_won']
data['rank']=data['diff'].rank(method='first',ascending=True)
data=data.sort_values('rank')
