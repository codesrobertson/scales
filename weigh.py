import json
import requests
from bs4 import BeautifulSoup as bs
from textblob import TextBlob

class Weigh:

  #method to get the url entered in the html form 
  def get_url(self, url):
    return url

  def get_article_title(self, url):
    dirty_text = requests.get(url).text
    soup = bs(dirty_text, 'html.parser')

    title = soup.find('h1')

    return title.text

  def get_article_contents(self, url):
    dirty_text = requests.get(url).text
    soup = bs(dirty_text, 'html.parser')

    text = soup.find_all('p')
    cleaned_text = []
    for p in text:
      cleaned_text.append(p.text)
    return "".join(cleaned_text)

  def get_request_body(self, url):
    return {
      "url": url,
      "title": self.get_article_title(url),
      "contents: ": self.get_article_contents(url)
    }

  def make_request(self, data):
    #Use requests library to return request
    r = requests.post('http://a8db28a19f13.ngrok.io/fakebox/check', json=data)

    if r.status_code != 200:
      print("Sorry, that link didn't work. Please ensure that the whole link was copied into the form box.")
      return {}

    return json.loads(r.text)

  #Method to return title score
  def get_title_score(self, json_dictionary):
    if "title" not in json_dictionary or "score" not in json_dictionary['title']:
      return 0

    title_score = json_dictionary['title']['score']

    return title_score

  def get_title_decision(self, json_dictionary):
    if "title" not in json_dictionary or "decision" not in json_dictionary['title']:
      return "none"

    title_decision = json_dictionary['title']['decision']

    return title_decision

  # Method to return content score
  def get_content_score(self, json_dictionary):
    if "content" not in json_dictionary or "score" not in json_dictionary['content']:
      return 0

    content_score = json_dictionary['content']['score']

    return content_score

  def get_content_decision(self, json_dictionary):
    if "content" not in json_dictionary or "decision" not in json_dictionary['content']:
      return "none"
      
    content_decision = json_dictionary['content']['decision']

    return content_decision

  def get_domain_category(self, json_dictionary):
    domain_category = json_dictionary['domain']['category']

    return domain_category

  def return_analysis(self, url):
    data = self.get_request_body(url)

    response = self.make_request(data)

    title_score = self.get_title_score(response)
    title_decision = self.get_title_decision(response)
    content_score = self.get_content_score(response)
    content_decision = self.get_content_decision(response)
    domain_category = self.get_domain_category(response)

    analysis = {
      "title_score": title_score,
      "title_decision": title_decision,
      "content_score": content_score,
      "content_decision": content_decision,
      "domain_category": domain_category,
      "overall_polarity": self.analyze_overall_polarity(url),
      "overall_subjectivity": self.analyze_overall_subjectivity(url),
      "average_bias": self.average_bias(url)
    }

    return analysis

  #Method to return request success
  def get_request_status(self, url):
    data = {}
    data['success'] = "success"

    r = requests.post('http://a8db28a19f13.ngrok.io/fakebox/check', json=data)

    json_dictionary = json.loads(r.text)

    status = json_dictionary['success']

    return status

  # Method to apply TextBlob to extracted whole text
  def analyze_overall_polarity(self, url):
    pre_polarity = self.get_article_contents(url)

    post_polarity = TextBlob(pre_polarity).sentiment.polarity

    return post_polarity

  def analyze_overall_subjectivity(self, url):
    pre_subjectivity = self.get_article_contents(url)

    post_subjectivity = TextBlob(pre_subjectivity).sentiment.subjectivity

    return post_subjectivity

  #Method to apply polarity analysis on a sentence-by-sentence level

  #Method to apply subjectivity analysis on a sentence by sentence level

  #START OF COMBO METHODS

  # Method to return percentage from FB and TB
  def average_bias(self, url):
    fakebox_score = self.get_content_score(url)
    textblob_score = self.analyze_overall_subjectivity(url)

    fakebox_score = int(fakebox_score)
    textblob_score = int(textblob_score)

    final_score = (fakebox_score + textblob_score)/2

    return final_score


Weigh().return_analysis('https://www.cnn.com/2020/07/21/politics/mitch-mcconnell-direct-payments-gop-plan/index.html')
