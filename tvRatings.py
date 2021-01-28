#%%
import requests
import json
# %%
#from config import connectionString
#%%
connectionString = {
    'url' : ' http://numbersapi.com/',
    'urlTV' : 'https://api.tvmaze.com/'
}
#%%

baseUrl = connectionString['urlTV']
# %%
endPoint = 'singlesearch/shows'
# %%
url = f'{baseUrl}{endPoint}'
# %%
class myError(Exception):
    def __init__(self, message, expression):
        self.message = message
        self.expression = expression
#%%

#list of tv show titles to query
tv_shows = ["Altered Carbon", "Grey's Anatomy", "This is Us", "The Flash", "Vikings", "Shameless", "Arrow", "Peaky Blinders", "Dirk Gently", "2345234523452345"]
#%%
class TvShow():
    def __init__(self, showName, rating) -> None:
        self.showName = showName
        self.rating = rating
#%%
try:

    for show in tv_shows:
        requestUrl = f'{url}?q={show}'

        response = requests.get(requestUrl)\
        if response.status_code == 200:
            response_json = response.json()
            print(response_json)
            showRatingList.append(TvShow(showName=show, rating response_json['rating']['average']))
        else:
            raise myError('Status Code: ', response.status_code)
except myError as e:
    print(f'{e.message}{e.expression}')        
# %%
for tv