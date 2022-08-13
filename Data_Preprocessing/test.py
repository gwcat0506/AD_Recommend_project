import pandas as pd
import numpy as np
from tqdm import tqdm

st_loc = pd.read_csv('C://Users//gwcat//Downloads//station_coordinate.csv')
print('1')
df = pd.read_csv('C://Users//gwcat//Downloads//Total_Bicycle.csv', encoding='utf8')
print('2')
st_loc.head(5)
df.head(5)