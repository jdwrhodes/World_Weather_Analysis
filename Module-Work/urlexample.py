#%% 
import requests
import json
#%%
#from config import connectionString
#%%
connectionString = {
    'url' : ' http://numbersapi.com/'
}
# %%
baseUrl = connectionString['url']
# %%
requestEndPoint = f'{baseUrl}17/trvia?json'

# %%
response = requests.get(requestEndPoint)
# %%
response.content
# %%
response_json = response.json()
# %%
response_json['text']
# %%
