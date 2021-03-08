#%%
import os
import json
# %%
filePath = './youtube_response.json'
# %%
with open(filePath, 'r') as fileHandle:
    responseJson = json.load(fileHandle)
# %%
responseJson['data']['itemsPerPage']
# %%
responseJson['data']['items'][0]['tags'][0]
# %%
responseJson['data']['items'][0]['content']['6']
# %%
