# !/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/pip(python 3.8)

from flask import Flask, render_template, url_for
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup


app = Flask(__name__, static_url_path="")

@app.route("/")
def index(): 
  return app.send_static_file("index.html")

if __name__ == "__main__":
  app.run(debug=True)


with open("index.html") as fp:
  soup = BeautifulSoup(fp)

soup = BeautifulSoup("<html>a web page</html>")

result = requests.get("https://www.google.com/")
print(result.status_code)


@result.route("/scales")
def result():
  return app.send_static_file("index.html")
