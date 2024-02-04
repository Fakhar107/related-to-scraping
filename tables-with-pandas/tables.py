import pandas as pd

df = pd.read_html('https://fastestlaps.com/tracks/le-mans-bugatti')
# df = pd.read_html('https://fastestlaps.com/tracks/le-mans-bugatti', parse_dates = True)
# df = pd.read_html('https://fastestlaps.com/tracks/le-mans-bugatti', skiprows=2 )
# df = pd.read_html('https://fastestlaps.com/tracks/le-mans-bugatti', match= )

print(df)
# below wil print first table in the page. 
# print(df[0])
# below code will print top 15 rows of table.
# print(df.head(15))
# df[0].to_csv(lsr.csv)
# etc
