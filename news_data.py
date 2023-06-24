from GoogleNews import GoogleNews
import pandas as pd
import requests
import json

# googlenews = GoogleNews(start='05/01/2020',end='05/31/2020')
# googlenews.search('Google')
# result = googlenews.result()
# df = pd.DataFrame(result)

# print(df.head())

user = 'adamu96'
page = ''
# response = requests.get(f'https://www.codewars.com/api/v1/users/{user}/code-challenges/completed?page={page}')
# completed_katas = pd.DataFrame(json.loads(response.content.decode('utf-8'))['data'])

response = requests.get(f'https://www.codewars.com/api/v1/users/{user}')
user_info = pd.DataFrame(json.loads(response.content.decode('utf-8')))
print(user_info.to_html())