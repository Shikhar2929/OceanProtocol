from datetime import datetime
import pandas as pd
df = pd.read_csv("ETH_DATA/eth_1_minute_price_techs.csv")

for index, row in df.iterrows():
    df['time'].iloc[index] = datetime.fromtimestamp(int(df['time'].iloc[index]) / 1000)
df.to_csv("ETH_DATA/eth_1_minute_price_techs_time.csv")
    #print(dt)
    #dt_object = datetime.fromtimestamp()
    #print(dt_object)
    #print(dt)
    #int(df['time'].iloc[index])