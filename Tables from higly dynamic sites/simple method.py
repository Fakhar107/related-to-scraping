import requests

url = 'https://api.dtm.com/data?query=wigeStandings&raceSeries=DTM&startDate=2021-12-31&endDate=2022-12-30&lang=en'

resp = requests.get(url)

print(resp.json())