import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.npr.org/sections/live-updates-protests-for-racial-justice/2020/07/08/889215893/transcripts-of-police-body-cams-show-floyd-pleaded-20-times-that-he-couldnt-brea'

response = requests.get(url).text

soup = bs(response, 'html.parser')

article = soup.find_all('p')
for p in article:
  print(p.text)
