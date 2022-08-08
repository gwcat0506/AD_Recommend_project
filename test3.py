import pandas as pd

area = [2600, 3000, 3200, 3600, 4000]
price = [550000, 565000, 610000, 680000, 725000]


df = pd.DataFrame((zip(area,price)) ,columns = ['area','price'])
print(df)



