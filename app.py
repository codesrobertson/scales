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
