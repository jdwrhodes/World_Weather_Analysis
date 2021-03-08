#%%
import requests
from config import connectionString
from pprint import pprint
# %%
# https://api.nytimes.com/svc/search/v2/articlesearch.json?q=election&api-key=yourkey

gameStopSpellings = ['Game Stop', 'Gamestop', 'gamestop', 'game stop']

baseUrl = 'https://api.nytimes.com/'
endPoint = 'svc/search/v2/articlesearch.json'
queryTerm = 'GameStop'
apiKey = connectionString['nytApiKey']
filter = "pub_date:(2021-01-01)"

# %%
queryUrl = f'{baseUrl}{endPoint}?q={queryTerm}&fq={filter}&api-key={apiKey}'
# %%
response = requests.get(queryUrl)
# %%
response
# %%
print(response)
# %%
response = response.json()
# %%
pprint(response)
# %%
print(queryUrl)
# %%
