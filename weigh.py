import json
import requests
from bs4 import BeautifulSoup as bs

#method to get the url entered in the html form 
def get_url(url):
  print(url)

#method to make a post request to FakeBox and return its result
def make_request(url):

  url = 'https://www.npr.org/sections/live-updates-protests-for-racial-justice/2020/07/08/889215893/transcripts-of-police-body-cams-show-floyd-pleaded-20-times-that-he-couldnt-brea'

  headers = {'Content-Type': "application/x-www-form-urlencoded; charset = utf-8",
             'Accept': "application/x-www-form-urlencoded; charset = utf-8"}

  #Make dictionary to store request
  data = {}
  data['url'] = "url"
  data['title'] = "title"
  data['content'] = "content"
  data['domain'] = "domain"

  #Use requests library to return request
  r = requests.post('http://a8db28a19f13.ngrok.io/fakebox/check', json = data)
  print(r.text)
  return r

make_request('https://www.npr.org/sections/live-updates-protests-for-racial-justice/2020/07/08/889215893/transcripts-of-police-body-cams-show-floyd-pleaded-20-times-that-he-couldnt-brea')


# Method to return "decision"



# Method to extract text from url submission

# Method to apply TextBlob to extracted text

# Method to return analyzed text
