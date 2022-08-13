import pandas as pd
import numpy as np
from tqdm import tqdm

st_loc = pd.read_csv('C://Users//gwcat//Downloads//station_coordinate.csv')
print('1')
df = pd.read_csv('C://Users//gwcat//Downloads//Total_Bicycle.csv', encoding='utf8')
print('2')
# st_loc.head(5)
# df.head(5)

df3 = df[['대여 대여소명','대여소 위도','대여소 경도']]
df3.drop_duplicates()

df3.reset_index(drop=True,inplace=True)

df_diff_rental = pd.DataFrame()
df_diff_return = pd.DataFrame()
station = []
diff_rental = []
diff_return = []
df3_rank1_station_rental = []
df3_rank1_diff_rental = []
df3_rank2_station_rental = []
df3_rank2_diff_rental = []
df3_rank1_station_return = []
df3_rank1_diff_return = []
df3_rank2_station_return = []
df3_rank2_diff_return = []
ex = pd.DataFrame()

for i in tqdm(range(len(df3))):
    # print("i : ",i)
    for j in range(len(st_loc)):
        station.append(st_loc['name'][j])
        diff_rental.append(np.sqrt((df3['대여소 위도'][i]-st_loc['lat'][j])**2 +
                            (df3['대여소 경도'][i]-st_loc['lng'][j])**2))
    ex['역'] = station
    ex['대여'] = diff_rental
    df_diff_rental['역(대여)'] = station
    df_diff_rental['차이(대여)'] = diff_rental
    df_diff_rental.sort_values('차이(대여)', inplace=True)
    df3_rank1_station_rental.append(df_diff_rental.iloc[0]['역(대여)'])
    df3_rank1_diff_rental.append(df_diff_rental.iloc[0]['차이(대여)'])
    df3_rank2_station_rental.append(df_diff_rental.iloc[1]['역(대여)'])
    df3_rank2_diff_rental.append(df_diff_rental.iloc[1]['차이(대여)'])

    station = []
    diff_rental = []
    diff_return = []
    
df3['1순위(대여)'] = df3_rank1_station_rental
df3['1순위 차이(대여)'] = df3_rank1_diff_rental
df3['2순위(대여)'] = df3_rank2_station_rental
df3['2순위 차이(대여)'] = df3_rank2_diff_rental

df3

df3.to_csv("data.csv", index = False)