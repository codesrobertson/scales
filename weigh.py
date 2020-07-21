import json
import requests
from bs4 import BeautifulSoup as bs
from textblob import TextBlob

class Weigh:

  #method to get the url entered in the html form 
  def get_url(self, url):
    return url

  #START OF FAKEBOX METHODS
  #method to make a post request to FakeBox and return its result
  def make_request(self, url):

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

    if r.status_code != 200:
      print("Sorry, that link didn't work. Please ensure that the whole link was copied into the form box.")

    return r

  #Method to return request success
  def get_request_status(self, url):
    data = {}
    data['success'] = "success"

    r = requests.post('http://a8db28a19f13.ngrok.io/fakebox/check', json=data)

    json_dictionary = json.loads(r.text)

    status = json_dictionary['success']

    return status

  #Method to return title score
  def get_title_score(self, url):
    data = {}
    data['title'] = "title"

    r = requests.post('http://a8db28a19f13.ngrok.io/fakebox/check', json=data)

    json_dictionary = json.loads(r.text)

    title_score = json_dictionary['title']['score']

    return title_score

  def get_title_decision(self, url):
    data = {}
    data['title'] = "title"

    r = requests.post('http://a8db28a19f13.ngrok.io/fakebox/check', json = data)

    json_dictionary = json.loads(r.text)

    title_decision = json_dictionary['title']['decision']

    return title_decision

  # Method to return content score
  def get_content_score(self, url):
    data = {}
    data['content'] = "content"

    r = requests.post('http://a8db28a19f13.ngrok.io/fakebox/check', json=data)

    json_dictionary = json.loads(r.text)

    content_score = json_dictionary['content']['score']

    return content_score

  def get_content_decision(self, url):
    data = {}
    data['content'] = "content"

    r = requests.post('http://a8db28a19f13.ngrok.io/fakebox/check', json=data)

    json_dictionary = json.loads(r.text)

    content_decision = json_dictionary['content']['decision']

    return content_decision

  #END OF FAKEBOX METHODS
  #START OF BS4/TEXTBLOB METHODS

  # Method to extract whole text from url submission and scrape with bs4
  def analyze_whole_text(self, url):
    dirty_text = requests.get(url).text
    soup = bs(dirty_text, 'html.parser')

    text = soup.find_all('p')
    cleaned_text = []
    for p in text:
      cleaned_text.append(p.text)
    return "".join(cleaned_text)

  # Method to apply TextBlob to extracted whole text
  def analyze_overall_polarity(self, url):
    pre_polarity = self.analyze_whole_text(url)

    post_polarity = TextBlob(pre_polarity).sentiment.polarity

    return post_polarity

  def analyze_overall_subjectivity(self, url):
    pre_subjectivity = self.analyze_whole_text(url)

    post_subjectivity = TextBlob(pre_subjectivity).sentiment.subjectivity

    return post_subjectivity

  #Method to apply polarity analysis on a sentence-by-sentence level

  #Method to apply subjectivity analysis on a sentence by sentence level

  #START OF COMBO METHODS

  # Method to return percentage from FB and TB
  def average_bias(self, url):
    fakebox_score = self.get_content_score(url)
    textblob_score = self.analyze_overall_subjectivity(url)

    final_score = (fakebox_score + textblob_score)/2

    return final_score

  def return_analysis(self, url):
    analysis = {}

    analysis['status'] = self.get_request_status(url)
    analysis['title_score'] = self.get_title_score(url)
    analysis['title_decision'] = self.get_title_decision(url)
    analysis['content_score'] = self.get_content_score(url)
    analysis['content_decision'] = self.get_content_decision(url)
    analysis['overall_polarity'] = self.analyze_overall_polarity(url)
    analysis['overall_subjectivity'] = self.analyze_overall_subjectivity(url)
    analysis['average_bias'] = self.average_bias(url)

    print(analysis)
    return analysis 


Weigh().return_analysis('https://www.npr.org/sections/live-updates-protests-for-racial-justice/2020/07/08/889215893/transcripts-of-police-body-cams-show-floyd-pleaded-20-times-that-he-couldnt-brea')
