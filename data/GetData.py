import pytse_client as tse
import pandas as pd

tse.download(symbols=["فملی"], write_to_csv=True)


#New data in old format:
data = pd.read_csv('tickers_data/فملی.csv') 
data.drop('yesterday', inplace=True, axis=1) 

data.to_csv('tickers_data/femeli-daily.csv', encoding='utf-8', index=False)