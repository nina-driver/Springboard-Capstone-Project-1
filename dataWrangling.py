import pandas as pd

wh_2015 = pd.read_csv('worldHappiness2015.csv', index_col=0)
wh_2016 = pd.read_csv('worldHappiness2016.csv', index_col=0)
wh_2017 = pd.read_csv('worldHappiness2017.csv', index_col=0)

print(wh_2015.head(10))
print(wh_2017.loc[:,'Happiness.Rank'])

