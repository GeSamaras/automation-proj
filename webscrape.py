import pandas as pd

df_csvtable = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv') #pd.read_html to get html as input
print('df_csvtable')

df_csvtable = df_csvtable.rename(columns={'Date':'date',
                                            'HomeTeam':'home_team',
                                            'AwayTeam':'away_team',
                                            'FTHG': 'home_goals',
                                            'FTAG': 'away_goals'})
