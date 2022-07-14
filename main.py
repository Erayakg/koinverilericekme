from binance.client import Client
import pandas as pd
from datetime import date as dt
client = Client(None,None)
print("Coin adı giriniz(Lütfen Büyük harflerle giriniz):")
prices = client.get_all_tickers()
CoinName=input()
periyotlar=[
    '1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']
print("İstediğiniz Periyodu giriniz(lütfen aşşağıdakilerden seçiniz):")

print(periyotlar)
Peryot=input()

def zamanhesapla(timestap):
    return dt.fromtimestamp(timestap/1000)

timestamp = client._get_earliest_valid_timestamp(CoinName, Peryot)
bars = client.get_historical_klines(CoinName, Peryot, timestamp, limit=1000)

for line in bars:
    del line[6:]

btc_df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close','Volume'])
btc_df.set_index('date', inplace=True)
btc_df.to_csv(f'{CoinName}.csv')

def veridüzenleme(csvDosya):
    newCvs=pd.read_csv(csvDosya)
    df1 = newCvs['date']
    for i in range(len(df1)):
        df1[i]=zamanhesapla(df1[i]);

    newCvs.to_csv(f'{CoinName}.csv',index=False)

veridüzenleme(f'{CoinName}.csv')



